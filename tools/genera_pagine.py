#!/usr/bin/env python3
"""Genera le due pagine del sito (italiano e inglese) da README.it.md e README.md.

Il repository e' l'unica fonte: le pagine non si modificano a mano.

Uso (dalla cartella del repository):
    python tools/genera_pagine.py                 # scrive nel sito (percorso di default)
    python tools/genera_pagine.py --sito <cartella del sito>
    python tools/genera_pagine.py --controlla     # solo verifiche, non scrive nulla

Scrive:
    <sito>/open-medical-informatics/index.html        (italiano)
    <sito>/en/open-medical-informatics/index.html     (inglese)
    <sito>/css/curriculum.css   e   <sito>/js/curriculum.js  (copiati da tools/modello/)

Solo libreria standard di Python. L'output e' deterministico: due esecuzioni
di fila producono file identici.

Identificatori dei corsi: ogni corso ha un id stabile, derivato dal livello e
dal nome italiano (es. "l1-python-for-everybody"). I due README devono avere
gli stessi corsi nello stesso ordine: l'n-esimo corso di una sezione inglese
prende l'id dell'n-esimo corso della stessa sezione italiana, cosi' gli id
sono uguali nelle due lingue e l'avanzamento salvato nel browser vale per
entrambe. Se si rinomina un corso in italiano il suo id cambia (e chi lo aveva
spuntato lo perde): in tal caso conviene esportare e reimportare l'avanzamento.
"""

import argparse
import hashlib
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SITE = ROOT.parent / "siti-web" / "dilettafalcone.it"
MODELLO = ROOT / "tools" / "modello"

SITE_URL = "https://dilettafalcone.it"
REPO_URL = "https://github.com/dilfalmd/open-medical-informatics"
STYLE_VERSION = "2"  # ?v=N di /css/style.css, come nelle altre pagine del sito
STORAGE_KEY = "omi-progress-v1"
PATH_IT = "/open-medical-informatics/"
PATH_EN = "/en/open-medical-informatics/"

LANGS = {
    "it": {
        "file": "README.it.md",
        "html_lang": "it",
        "og_locale": "it_IT",
        "og_alt_locale": "en_US",
        "path": PATH_IT,
        "title": "Open Medical Informatics - Diletta Falcone",
        "description": "Curriculum gratuito, sul modello di OSSU Computer Science, per medici che vogliono diventare medici informatici: sei livelli, due indirizzi, fonti citate e caselle di avanzamento.",
        "og_image_alt": "Diletta Falcone, medico chirurgo",
        "nav": [("Percorso", "/percorso/"), ("Progetti", "/progetti/"), ("Contatti", "#contatti")],
        "switch": ("English", PATH_EN, "en"),
        "eyebrow": "// curriculum gratuito",
        "repo_label": "Repository",
        "license_label": "Licenza CC BY-SA 4.0",
        "license_url": "https://creativecommons.org/licenses/by-sa/4.0/deed.it",
        "tracker_title": "Il tuo avanzamento",
        "tracker_note": "Spunta i corsi che hai finito. L'avanzamento si salva solo in questo browser (stessi dati nella versione italiana e inglese); le voci facoltative non contano nelle barre. Per cambiare dispositivo esporta il file e importalo dall'altra parte.",
        "bar_core": "Tronco comune (livelli 0–5)",
        "bar_core_a": "Tronco comune + Indirizzo A",
        "bar_core_b": "Tronco comune + Indirizzo B",
        "btn_export": "Esporta avanzamento",
        "btn_import": "Importa avanzamento",
        "btn_reset": "Azzera",
        "toc_label": "Indice della pagina",
        "noscript": "JavaScript non è attivo: le caselle non vengono salvate.",
        "msg": {
            "storage_corrupt": "I dati salvati nel browser non sono leggibili: avanzamento azzerato.",
            "storage_unavailable": "Il salvataggio nel browser non è disponibile: l'avanzamento resta solo finché la pagina è aperta. Usa «Esporta avanzamento» per conservarlo.",
            "exported": "File esportato.",
            "export_error": "Non è stato possibile creare il file.",
            "imported": "Avanzamento importato: {n} corsi spuntati.",
            "imported_unknown": "Avanzamento importato: {n} corsi spuntati ({u} voci sconosciute ignorate).",
            "import_error": "File non valido: non è un avanzamento di Open Medical Informatics.",
            "reset_confirm": "Azzerare tutto l'avanzamento?",
            "reset_done": "Avanzamento azzerato.",
            "done_word": "completati",
        },
        "footer_name": "Diletta Falcone",
    },
    "en": {
        "file": "README.md",
        "html_lang": "en",
        "og_locale": "en_US",
        "og_alt_locale": "it_IT",
        "path": PATH_EN,
        "title": "Open Medical Informatics - Diletta Falcone",
        "description": "A free curriculum, modelled on OSSU Computer Science, for physicians who want to become clinical informaticians: six levels, two tracks, cited sources and progress checkboxes.",
        "og_image_alt": "Diletta Falcone, physician",
        "nav": [("Background", "/percorso/"), ("Projects", "/progetti/"), ("Contact", "#contatti")],
        "switch": ("Italiano", PATH_IT, "it"),
        "eyebrow": "// free curriculum",
        "repo_label": "Repository",
        "license_label": "CC BY-SA 4.0 license",
        "license_url": "https://creativecommons.org/licenses/by-sa/4.0/deed.en",
        "tracker_title": "Your progress",
        "tracker_note": "Tick the courses you have finished. Progress is saved only in this browser (the same data in the Italian and English versions); optional entries do not count in the bars. To move to another device, export the file and import it there.",
        "bar_core": "Common core (levels 0–5)",
        "bar_core_a": "Common core + Track A",
        "bar_core_b": "Common core + Track B",
        "btn_export": "Export progress",
        "btn_import": "Import progress",
        "btn_reset": "Reset",
        "toc_label": "Page contents",
        "noscript": "JavaScript is off: the checkboxes will not be saved.",
        "msg": {
            "storage_corrupt": "The data saved in the browser cannot be read: progress has been reset.",
            "storage_unavailable": "Saving in the browser is not available: progress is kept only while this page is open. Use \"Export progress\" to keep it.",
            "exported": "File exported.",
            "export_error": "The file could not be created.",
            "imported": "Progress imported: {n} courses ticked.",
            "imported_unknown": "Progress imported: {n} courses ticked ({u} unknown entries ignored).",
            "import_error": "Invalid file: it is not an Open Medical Informatics progress file.",
            "reset_confirm": "Reset all progress?",
            "reset_done": "Progress reset.",
            "done_word": "done",
        },
        "footer_name": "Diletta Falcone",
    },
}

# Riconoscimento delle sezioni dal titolo H2 (in entrambe le lingue).
SECTION_PATTERNS = [
    ("level", re.compile(r"^(?:Livello|Level)\s+(\d)\b")),
    ("track", re.compile(r"^(?:Indirizzo|Track)\s+([AB])\b")),
    ("electives", re.compile(r"^(?:Approfondimenti|Electives)\b")),
    ("projects", re.compile(r"^(?:Progetto finale|Final project)\b")),
    ("references", re.compile(r"^(?:Bibliografia|References)\b")),
]
COURSE_COLS = 8
OPTIONAL_RE = re.compile(r"^\*\((?:facoltativo|optional)\b")
PROJECT_RE = re.compile(r"^\*\*([AB]) · (.+?)\*\*\s*(.*)$", re.S)
REVISION_RE = re.compile(r"^(?:Ultima revisione|Last revised):", re.I)


class Errori(Exception):
    pass


# --------------------------------------------------------------------------
# Lettura del Markdown
# --------------------------------------------------------------------------

def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def starts_block(line):
    return bool(
        re.match(r"^#{1,3}\s", line)
        or line.startswith("|")
        or line.startswith("- ")
        or re.match(r"^\d+\.\s", line)
        or re.match(r"^-{3,}\s*$", line)
    )


def parse_blocks(text):
    lines = text.replace("\r\n", "\n").split("\n")
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            blocks.append(("h", len(m.group(1)), m.group(2).strip()))
            i += 1
            continue
        if re.match(r"^-{3,}\s*$", line):
            blocks.append(("hr",))
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            blocks.append(("table", rows))
            continue
        if re.match(r"^\d+\.\s", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i]):
                m = re.match(r"^(\d+)\.\s+(.*)$", lines[i])
                items.append((int(m.group(1)), m.group(2).strip()))
                i += 1
            blocks.append(("ol", items))
            continue
        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:].strip())
                i += 1
            blocks.append(("ul", items))
            continue
        buf = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not starts_block(lines[i]):
            buf.append(lines[i].strip())
            i += 1
        blocks.append(("p", " ".join(buf)))
    return blocks


def slugify(text, max_len=44):
    text = re.sub(r"\*+", "", text)
    text = re.sub(r"\([^)]*\)", " ", text)  # via le parentesi
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0] or text[:max_len]
    return text or "voce"


class Section:
    def __init__(self, title, kind, key):
        self.title = title
        self.kind = kind  # level, track, electives, projects, references, generic
        self.key = key  # l0..l5, a, b, ap, ...
        self.blocks = []
        self.courses = []  # per le sezioni con tabella dei corsi
        self.projects = []
        self.refs = []


class Doc:
    pass


def parse_doc(path):
    blocks = parse_blocks(path.read_text(encoding="utf-8"))
    doc = Doc()
    doc.path = path
    doc.title = None
    doc.intro = []
    doc.sections = []
    seen_h1 = False
    cur = None
    for b in blocks:
        if b[0] == "h" and b[1] == 1 and not seen_h1:
            seen_h1 = True
            doc.title = b[2]
            continue
        if not seen_h1:
            continue  # righe prima del titolo (link cambio lingua): ignorate
        if b[0] == "h" and b[1] == 2:
            kind, key = "generic", slugify(b[2], 30)
            for k, rx in SECTION_PATTERNS:
                m = rx.match(b[2])
                if m:
                    kind = k
                    if k == "level":
                        key = "l" + m.group(1)
                    elif k == "track":
                        key = m.group(1).lower()
                    elif k == "electives":
                        key = "ap"
                    else:
                        key = k
                    break
            cur = Section(b[2], kind, key)
            doc.sections.append(cur)
            continue
        if b[0] == "hr":
            continue
        (cur.blocks if cur else doc.intro).append(b)
    if doc.title is None:
        raise Errori("%s: manca il titolo H1" % path.name)
    extract(doc)
    return doc


def extract(doc):
    """Estrae corsi, progetti e bibliografia dalle sezioni."""
    for s in doc.sections:
        if s.kind in ("level", "track", "electives"):
            tables = [b for b in s.blocks if b[0] == "table" and len(b[1][0]) == COURSE_COLS]
            if len(tables) != 1:
                raise Errori("%s: la sezione «%s» deve avere una sola tabella dei corsi" % (doc.path.name, s.title))
            rows = tables[0][1]
            s.table_block = tables[0]
            s.headers = rows[0]
            for r in rows[2:]:
                if len(r) != COURSE_COLS:
                    raise Errori("%s: riga con %d celle in «%s»: %s" % (doc.path.name, len(r), s.title, r[0][:40]))
                s.courses.append({"cells": r, "optional": bool(OPTIONAL_RE.match(r[0]))})
        elif s.kind == "projects":
            for b in s.blocks:
                if b[0] == "p":
                    m = PROJECT_RE.match(b[1])
                    if m:
                        s.projects.append({"letter": m.group(1), "title": m.group(2).rstrip(". "), "text": m.group(3)})
        elif s.kind == "references":
            for b in s.blocks:
                if b[0] == "ol":
                    s.refs = b[1]


# --------------------------------------------------------------------------
# Id dei corsi (dal testo italiano, uguali nelle due lingue)
# --------------------------------------------------------------------------

def assign_ids(it, en):
    ids = {}  # (lingua, chiave sezione, indice) -> id
    used = set()
    problems = []
    sec_en = {s.key: s for s in en.sections}
    for s in it.sections:
        if s.kind in ("level", "track", "electives"):
            e = sec_en.get(s.key)
            if e is None or len(e.courses) != len(s.courses):
                problems.append("sezione «%s»: %d corsi in italiano, %s in inglese" % (
                    s.title, len(s.courses), "nessuna sezione" if e is None else len(e.courses)))
                continue
            for i, c in enumerate(s.courses):
                base = "%s-%s" % (s.key, slugify(c["cells"][0]))
                cid, n = base, 2
                while cid in used:
                    cid = "%s-%d" % (base, n)
                    n += 1
                used.add(cid)
                ids[("it", s.key, i)] = cid
                ids[("en", s.key, i)] = cid
                if c["optional"] != e.courses[i]["optional"]:
                    problems.append("corso %d di «%s»: facoltativo in una lingua sola" % (i + 1, s.title))
        elif s.kind == "projects":
            e = sec_en.get("projects")
            li = [p["letter"] for p in s.projects]
            le = [p["letter"] for p in e.projects] if e else []
            if li != le:
                problems.append("progetti finali diversi: %s / %s" % (li, le))
            for i, p in enumerate(s.projects):
                pid = "progetto-" + p["letter"].lower()
                ids[("it", "projects", i)] = pid
                ids[("en", "projects", i)] = pid
    return ids, problems


# --------------------------------------------------------------------------
# Inline Markdown -> HTML
# --------------------------------------------------------------------------

def esc(s):
    return html.escape(s, quote=True)


def fix_url(url):
    if url in ("README.md", "README.it.md", "CONTRIBUTING.md", "LICENSE"):
        return "%s/blob/main/%s" % (REPO_URL, url)
    return url


LINK_RE = re.compile(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)(?:\s+"([^"]*)")?\)')
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")


def check_url(url):
    """Ammette solo http://, https://, mailto:, ancore (#) e percorsi relativi."""
    if re.search(r"[\x00-\x20\x7f]", url):
        raise Errori("indirizzo non ammesso (caratteri di controllo o spazi): %r" % url)
    if url.startswith("#"):
        return url
    low = url.lower()
    if low.startswith(("http://", "https://")) and len(url) > 8:
        return url
    if low.startswith("mailto:") and len(url) > 7:
        return url
    if SCHEME_RE.match(url) or url.startswith("//"):
        raise Errori("indirizzo non ammesso (solo http://, https://, mailto:, ancore e percorsi relativi): %s" % url)
    return url


def inline(s, links=True, _tokens=None):
    tokens = _tokens if _tokens is not None else []

    def stash(h):
        tokens.append(h)
        return "\x00%d\x00" % (len(tokens) - 1)

    s = re.sub(r"`([^`]+)`", lambda m: stash("<code>%s</code>" % esc(m.group(1))), s)

    if links:
        def md_link(m):
            url = fix_url(check_url(m.group(2)))
            title = ' title="%s"' % esc(m.group(3)) if m.group(3) else ""
            # il testo del link condivide i token del codice gia' messo da parte
            return stash('<a href="%s"%s>%s</a>' % (esc(url), title, inline(m.group(1), links=False, _tokens=tokens)))
        s = LINK_RE.sub(md_link, s)

        def bare(m):
            url = m.group(0)
            tail = ""
            while url and url[-1] in ".,;:)":
                if url[-1] == ")" and "(" in url:
                    break
                tail = url[-1] + tail
                url = url[:-1]
            return stash('<a href="%s">%s</a>' % (esc(url), esc(url))) + tail
        s = re.sub(r"https?://[^\s<>\"]+", bare, s)

    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    if links:
        s = re.sub(r"\[(\d+)\]", r'<a class="cit" href="#ref-\1">[\1]</a>', s)
    if _tokens is None:
        while "\x00" in s:
            s = re.sub(r"\x00(\d+)\x00", lambda m: tokens[int(m.group(1))], s)
    return s


def plain(s):
    """Testo senza Markdown (per attributi e controlli)."""
    s = LINK_RE.sub(r"\1", s)
    return re.sub(r"[*`]", "", s)


# --------------------------------------------------------------------------
# Rendering della pagina
# --------------------------------------------------------------------------

def render_blocks(blocks, out, labels_skip=()):
    for b in blocks:
        t = b[0]
        if t == "p":
            out.append("<p>%s</p>" % inline(b[1]))
        elif t == "ul":
            out.append("<ul>" + "".join("<li>%s</li>" % inline(x) for x in b[1]) + "</ul>")
        elif t == "ol":
            out.append("<ol>" + "".join("<li>%s</li>" % inline(x) for _, x in b[1]) + "</ol>")
        elif t == "table":
            out.append(render_table(b[1]))
        elif t == "h":
            out.append("<h%d>%s</h%d>" % (b[1], inline(b[2]), b[1]))


def render_table(rows):
    head = rows[0]
    out = ['<div class="tabella"><table><thead><tr>']
    out += ["<th scope=\"col\">%s</th>" % inline(h) for h in head]
    out.append("</tr></thead><tbody>")
    for r in rows[2:]:
        out.append("<tr>")
        for h, c in zip(head, r):
            out.append('<td data-label="%s">%s</td>' % (esc(plain(h)), inline(c)))
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def split_heading(title):
    if " · " in title:
        a, b = title.split(" · ", 1)
        return a.strip(), b.strip()
    return "", title


def bar_html(name, groups, total, extra_class=""):
    return (
        '<div class="bar%s" data-groups="%s" data-total="%d">'
        '<div class="bar-label"><span class="bar-name">%s</span><span class="bar-num">0 / %d (0%%)</span></div>'
        '<div class="bar-track" role="progressbar" aria-label="%s" aria-valuemin="0" aria-valuemax="%d" aria-valuenow="0">'
        '<div class="bar-fill"></div></div></div>'
    ) % (extra_class, groups, total, esc(name), total, esc(name), total)


def count_group(doc, keys):
    n = 0
    for s in doc.sections:
        if s.kind in ("level", "track", "electives") and s.key in keys:
            n += sum(1 for c in s.courses if not c["optional"])
        if s.kind == "projects":
            n += sum(1 for p in s.projects if p["letter"].lower() in keys)
    return n


def render_page(lang, doc, ids, errors):
    L = LANGS[lang]
    other = "en" if lang == "it" else "it"
    out = []
    add = out.append

    # -- intestazione del documento ---------------------------------------
    url_self = SITE_URL + L["path"]
    url_it, url_en = SITE_URL + PATH_IT, SITE_URL + PATH_EN
    css_hash = file_hash(MODELLO / "curriculum.css")
    js_hash = file_hash(MODELLO / "curriculum.js")
    add("<!DOCTYPE html>")
    add('<html lang="%s">' % L["html_lang"])
    add("<head>")
    add('  <meta charset="UTF-8">')
    add('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    add('  <meta name="description" content="%s">' % esc(L["description"]))
    add("  <title>%s</title>" % esc(L["title"]))
    add('  <link rel="canonical" href="%s">' % url_self)
    add('  <link rel="alternate" hreflang="it" href="%s">' % url_it)
    add('  <link rel="alternate" hreflang="en" href="%s">' % url_en)
    add('  <link rel="alternate" hreflang="x-default" href="%s">' % url_it)
    add('  <link rel="icon" href="/favicon.svg" type="image/svg+xml">')
    add('  <link rel="icon" href="/favicon-96.png" sizes="96x96" type="image/png">')
    add('  <link rel="icon" href="/favicon.ico" sizes="any">')
    add('  <link rel="apple-touch-icon" href="/apple-touch-icon.png">')
    add('  <meta property="og:type" content="website">')
    add('  <meta property="og:site_name" content="Diletta Falcone">')
    add('  <meta property="og:locale" content="%s">' % L["og_locale"])
    add('  <meta property="og:locale:alternate" content="%s">' % L["og_alt_locale"])
    add('  <meta property="og:title" content="%s">' % esc(L["title"]))
    add('  <meta property="og:description" content="%s">' % esc(L["description"]))
    add('  <meta property="og:url" content="%s">' % url_self)
    add('  <meta property="og:image" content="%s/og-image.png">' % SITE_URL)
    add('  <meta property="og:image:width" content="1200">')
    add('  <meta property="og:image:height" content="630">')
    add('  <meta property="og:image:alt" content="%s">' % esc(L["og_image_alt"]))
    add('  <meta name="twitter:card" content="summary_large_image">')
    add('  <link rel="preconnect" href="https://fonts.googleapis.com">')
    add('  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    add('  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">')
    add('  <link rel="stylesheet" href="/css/style.css?v=%s">' % STYLE_VERSION)
    add('  <link rel="stylesheet" href="/css/curriculum.css?v=%s">' % css_hash)
    add("</head>")
    add("<body>")
    add("")

    # -- menu, come le altre pagine ---------------------------------------
    add("  <nav>")
    add('    <div class="nav-inner">')
    add('      <a href="/" class="nav-logo" aria-label="Diletta Falcone, home">DF</a>')
    add('      <ul class="nav-links">')
    for label, href in L["nav"]:
        add('        <li><a href="%s">%s</a></li>' % (href, esc(label)))
    sw_label, sw_href, sw_lang = L["switch"]
    add('        <li><a href="%s" lang="%s" hreflang="%s">%s</a></li>' % (sw_href, sw_lang, sw_lang, esc(sw_label)))
    add("      </ul>")
    add("    </div>")
    add("  </nav>")
    add("")
    add('  <main class="omi">')

    # -- testata ------------------------------------------------------------
    intro = list(doc.intro)
    lead = None
    meta_list = None
    rest = []
    for b in intro:
        if lead is None and b[0] == "p":
            lead = re.sub(r"^\*\*(.+)\*\*$", r"\1", b[1])
        elif meta_list is None and b[0] == "ul":
            meta_list = b[1]
        else:
            rest.append(b)
    if lead is None or meta_list is None:
        raise Errori("%s: dopo il titolo servono un paragrafo e un elenco (revisione, curatrice)" % doc.path.name)
    if not any(REVISION_RE.match(plain(x)) for x in meta_list):
        raise Errori("%s: manca la riga «Ultima revisione»/«Last revised»" % doc.path.name)
    add('    <section class="wrap page-head">')
    add('      <p class="eyebrow">%s</p>' % esc(L["eyebrow"]))
    add("      <h1>%s</h1>" % inline(doc.title))
    add('      <p class="lead">%s</p>' % inline(lead))
    add('      <ul class="meta-list">' + "".join("<li>%s</li>" % inline(x) for x in meta_list) + "</ul>")
    add('      <p class="repo-line"><a href="%s">%s</a></p>' % (REPO_URL, esc(L["repo_label"])))
    add("    </section>")
    add("")
    add('    <section class="wrap prose intro">')
    body = []
    render_blocks(rest, body)
    add("      " + "\n      ".join(body))
    add("    </section>")
    add("")

    # -- avanzamento --------------------------------------------------------
    core_keys = ["l0", "l1", "l2", "l3", "l4", "l5"]
    add('    <section class="wrap tracker-wrap" id="avanzamento">')
    add('      <div class="tracker">')
    add("        <h2>%s</h2>" % esc(L["tracker_title"]))
    add('        <div class="bars">')
    add("          " + bar_html(L["bar_core"], " ".join(core_keys), count_group(doc, core_keys)))
    add("          " + bar_html(L["bar_core_a"], " ".join(core_keys + ["a"]), count_group(doc, core_keys + ["a"])))
    add("          " + bar_html(L["bar_core_b"], " ".join(core_keys + ["b"]), count_group(doc, core_keys + ["b"])))
    add("        </div>")
    add('        <div class="tools">')
    add('          <button type="button" class="btn btn-primary" id="omi-export">%s</button>' % esc(L["btn_export"]))
    add('          <button type="button" class="btn" id="omi-import">%s</button>' % esc(L["btn_import"]))
    add('          <button type="button" class="btn" id="omi-reset">%s</button>' % esc(L["btn_reset"]))
    add('          <input type="file" id="omi-file" accept="application/json,.json" hidden>')
    add("        </div>")
    add('        <p class="tracker-note">%s</p>' % esc(L["tracker_note"]))
    add('        <p class="tracker-status" id="omi-status" role="status" aria-live="polite"></p>')
    add("        <noscript><p class=\"tracker-status\">%s</p></noscript>" % esc(L["noscript"]))
    add("      </div>")
    add("    </section>")
    add("")

    # -- indice -------------------------------------------------------------
    add('    <section class="wrap toc-wrap">')
    add('      <nav class="toc" aria-label="%s"><ul>' % esc(L["toc_label"]))
    for s in doc.sections:
        kicker, title = split_heading(s.title)
        label = kicker if kicker else title
        add('        <li><a href="#%s">%s</a></li>' % (section_id(s), inline(label)))
    add("      </ul></nav>")
    add("    </section>")
    add("")

    # -- sezioni --------------------------------------------------------------
    for s in doc.sections:
        sid = section_id(s)
        kicker, title = split_heading(s.title)
        add('    <section class="wrap section" id="%s">' % sid)
        if kicker:
            add('      <p class="kicker">%s</p>' % inline(kicker))
        add("      <h2>%s</h2>" % inline(title))

        if s.kind in ("level", "track", "electives"):
            groups = s.key
            total = count_group(doc, [s.key])
            add("      " + bar_html(kicker or title, groups, total, " bar-section"))
            body = []
            render_blocks([b for b in s.blocks if b is not s.table_block], body)
            add('      <div class="prose">' + "".join(body) + "</div>")
            add('      <div class="corsi">')
            for i, c in enumerate(s.courses):
                add(render_course(c, ids[(lang, s.key, i)], s.key, s.headers))
            add("      </div>")
            if s.kind == "track":
                # i progetti finali di questo indirizzo compaiono nella sezione «Progetto finale»
                pass
        elif s.kind == "projects":
            body = []
            n = 0
            for b in s.blocks:
                m = PROJECT_RE.match(b[1]) if b[0] == "p" else None
                if m:
                    p = s.projects[n]
                    body.append(render_project(p, ids[(lang, "projects", n)]))
                    n += 1
                else:
                    render_blocks([b], body)
            add('      <div class="prose">' + "".join(body) + "</div>")
        elif s.kind == "references":
            body = []
            for b in s.blocks:
                if b[0] == "ol":
                    body.append('<ol class="refs">')
                    for n, text in b[1]:
                        body.append('<li id="ref-%d" value="%d">%s</li>' % (n, n, inline(text)))
                    body.append("</ol>")
                else:
                    render_blocks([b], body)
            add('      <div class="prose">' + "".join(body) + "</div>")
        else:
            body = []
            render_blocks(s.blocks, body)
            add('      <div class="prose">' + "".join(body) + "</div>")
        add("    </section>")
        add("")

    add("  </main>")
    add("")
    add('  <footer id="contatti">')
    add('    <div class="footer-inner">')
    add('      <a href="mailto:info@dilettafalcone.it">info@dilettafalcone.it</a>')
    add('      <p>© 2026 %s · <a href="%s">%s</a></p>' % (esc(L["footer_name"]), esc(L["license_url"]), esc(L["license_label"])))
    add("    </div>")
    add("  </footer>")

    cfg = {"key": STORAGE_KEY, "lang": lang, "msg": L["msg"]}
    cfg_json = json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")
    add('  <script type="application/json" id="omi-config">%s</script>' % cfg_json)
    add('  <script src="/js/curriculum.js?v=%s" defer></script>' % js_hash)
    add("</body>")
    add("</html>")
    return "\n".join(out) + "\n"


def section_id(s):
    if s.kind in ("level", "track", "electives"):
        return "s-" + s.key
    return "s-" + s.key


def render_course(c, cid, key, headers):
    cells = c["cells"]
    opt = " data-optional=\"1\"" if c["optional"] else ""
    out = ['      <article class="corso%s" id="c-%s">' % (" facoltativo" if c["optional"] else "", cid)]
    out.append(
        '        <div class="corso-head"><input type="checkbox" class="chk" id="chk-%s" data-id="%s" data-group="%s"%s>'
        '<label for="chk-%s">%s</label></div>' % (cid, cid, key, opt, cid, inline(cells[0]))
    )
    out.append('        <dl class="meta">')
    wide = {1, 2, 7}  # Fonte, Tipo di fonte, Note
    for idx in range(1, COURSE_COLS):
        cls = "m m-wide" if idx in wide else "m"
        out.append('          <div class="%s"><dt>%s</dt><dd>%s</dd></div>' % (cls, esc(plain(headers[idx])), inline(cells[idx])))
    out.append("        </dl>")
    out.append("      </article>")
    return "\n".join(out)


def render_project(p, pid):
    letter = p["letter"]
    return (
        '<article class="corso progetto" id="c-%s">'
        '<div class="corso-head"><input type="checkbox" class="chk" id="chk-%s" data-id="%s" data-group="%s">'
        '<label for="chk-%s">%s · %s</label></div>'
        '<p class="progetto-testo">%s</p></article>'
    ) % (pid, pid, pid, letter.lower(), pid, esc(letter), inline(p["title"]), inline(p["text"]))


def file_hash(path):
    return hashlib.sha1(path.read_bytes()).hexdigest()[:8]


# --------------------------------------------------------------------------
# Controlli e scrittura
# --------------------------------------------------------------------------

def check(it, en, ids, page_it, page_en):
    errs = []
    for lang, doc, page in (("it", it, page_it), ("en", en, page_en)):
        refs = [s for s in doc.sections if s.kind == "references"]
        if not refs or not refs[0].refs:
            errs.append("%s: bibliografia mancante" % lang)
            continue
        nums = [n for n, _ in refs[0].refs]
        if nums != list(range(1, len(nums) + 1)):
            errs.append("%s: la bibliografia non e' numerata 1..N di seguito" % lang)
        anchors = set(re.findall(r'id="ref-(\d+)"', page))
        cited = set(int(x) for x in re.findall(r'class="cit" href="#ref-(\d+)"', page))
        missing = sorted(n for n in cited if str(n) not in anchors)
        if missing:
            errs.append("%s: rimandi senza ancora: %s" % (lang, missing))
        unused = sorted(n for n in nums if n not in cited)
        if unused:
            errs.append("%s: voci di bibliografia mai citate: %s" % (lang, unused))
    # stesse citazioni, nello stesso ordine, nelle due lingue
    def cite_seq(doc):
        seq = []
        for s in doc.sections:
            if s.kind in ("level", "track", "electives"):
                for c in s.courses:
                    seq.append(tuple(re.findall(r"\[(\d+)\](?!\()", " ".join(c["cells"]))))
        return seq
    if cite_seq(it) != cite_seq(en):
        errs.append("le citazioni dei corsi non coincidono tra italiano e inglese")
    boxes_it = len(re.findall(r'<input type="checkbox"', page_it))
    boxes_en = len(re.findall(r'<input type="checkbox"', page_en))
    if boxes_it != boxes_en:
        errs.append("caselle diverse: %d (it) contro %d (en)" % (boxes_it, boxes_en))
    id_it = re.findall(r'data-id="([^"]+)"', page_it)
    id_en = re.findall(r'data-id="([^"]+)"', page_en)
    if id_it != id_en:
        errs.append("gli id delle caselle non coincidono tra le due pagine")
    if len(set(id_it)) != len(id_it):
        errs.append("id duplicati")
    return errs, boxes_it, boxes_en


def write_if_changed(path, content, dry):
    path = Path(path)
    old = path.read_bytes() if path.exists() else None
    data = content.encode("utf-8")
    if old == data:
        return "invariato"
    if not dry:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    return "scritto" if old is not None else "creato"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--sito", default=str(DEFAULT_SITE), help="cartella del sito (default: %(default)s)")
    ap.add_argument("--controlla", action="store_true", help="solo verifiche, non scrive file")
    args = ap.parse_args(argv)
    site = Path(args.sito)

    try:
        it = parse_doc(ROOT / LANGS["it"]["file"])
        en = parse_doc(ROOT / LANGS["en"]["file"])
        ids, problems = assign_ids(it, en)
        if problems:
            raise Errori("README.it.md e README.md non sono paralleli:\n  - " + "\n  - ".join(problems))
        page_it = render_page("it", it, ids, [])
        page_en = render_page("en", en, ids, [])
        errs, n_it, n_en = check(it, en, ids, page_it, page_en)
    except Errori as e:
        print("ERRORE:", e, file=sys.stderr)
        return 1
    for e in errs:
        print("ERRORE:", e, file=sys.stderr)
    if errs:
        return 1

    n_courses = sum(len(s.courses) for s in it.sections)
    n_opt = sum(1 for s in it.sections for c in s.courses if c["optional"])
    print("corsi: %d (%d facoltativi); caselle: %d it, %d en; riferimenti: %d" % (
        n_courses, n_opt, n_it, n_en, max(n for s in it.sections for n, _ in s.refs)))

    dry = args.controlla
    jobs = [
        (site / "open-medical-informatics" / "index.html", page_it),
        (site / "en" / "open-medical-informatics" / "index.html", page_en),
        (site / "css" / "curriculum.css", (MODELLO / "curriculum.css").read_text(encoding="utf-8")),
        (site / "js" / "curriculum.js", (MODELLO / "curriculum.js").read_text(encoding="utf-8")),
    ]
    for path, content in jobs:
        print("%-9s %s" % ("(prova)" if dry else write_if_changed(path, content, False), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
