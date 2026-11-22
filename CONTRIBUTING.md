# Contributing

[Italiano](#contribuire)

Thank you for helping to keep **Open Medical Informatics** accurate and up to date. Every proposal is reviewed before it is merged. The curriculum itself is in [README.it.md](README.it.md) (Italian) and [README.md](README.md) (English): the two files must always contain the same courses in the same order.

## Source criteria

**Allowed**
- Universities, including Italian ones (for example Federica Web Learning, EduOpen).
- Standards bodies: HL7, DICOM/NEMA, SNOMED International, Regenstrief/LOINC, WHO/ICD, OHDSI.
- Institutions: WHO, European Commission and Parliament, Ministero della Salute, ISS, AGENAS, AgID, Garante per la protezione dei dati personali.
- Peer-reviewed literature (PubMed/PMC, EQUATOR Network).
- Scientific societies: AMIA, IMIA, EFMI.
- Recognised non-academic organisations (for example DeepLearning.AI, fast.ai, Google ML Crash Course, Kaggle Learn, Microsoft Learn, Hugging Face): these are labelled **Industry** in the "Source type" column, and only if the courses are free and by recognised authors.

**Excluded**
- Non-institutional blogs and YouTube channels.
- Vendor marketing material.
- **Preprints** that have not been peer reviewed: no exceptions.
- Paid resources (master's degrees, certifications, books). "Audit" courses are accepted only if the free access is verifiable, and they are flagged in the Notes.

## What every entry must contain

1. **Author or body** responsible for the resource.
2. **Link**. The verification date is not repeated in each entry: whoever checks the links updates the single date at the top of the READMEs ("Links verified on"), after opening each link and checking that the resource is free and still available.
3. **Source type**: University, Standards body, Institution, Peer-reviewed, Scientific society or Industry.
4. **Numbered citation in the References** in **Vancouver style**, in order of first appearance, with DOI and/or PMID for articles and the full details (title, number, date, Official Journal reference) for regulations. Every statement of fact in the curriculum (regulations, figures, definitions) must point to a numbered reference.
5. The usual columns: language, effort (marked "estimate" when it is not stated by the source), prerequisites, notes.

Courses, titles in the References and regulations keep their original form (language and wording); only our own descriptive text is translated.

## How to propose an entry or a correction

- **Issue:** open an issue with the link, the level or track where the resource belongs, the source type, and why it fits the criteria above. Also use issues to report a broken or outdated link, a wrong figure or a new revision of a regulation.
- **Pull request:** edit both [README.it.md](README.it.md) and [README.md](README.md) (same course, same position, same citation numbers), add the Vancouver entry at the right place in the References and renumber the following ones, and describe the change.
- Proposals that do not meet the criteria are closed with a short explanation.
- Do not post patient data anywhere, neither in the repository nor in issues.

After a change to the READMEs, the pages of the website are regenerated with `python tools/genera_pagine.py`.

## Review schedule

- **Links:** checked automatically every month (GitHub Actions, workflow "Link check", which opens an issue if it finds broken links). Pages that block bots (for example eur-lex.europa.eu) are excluded and checked by hand.
- **Content:** full review once a year; the "Revised" date at the top of the READMEs is updated when it is done.

---

# Contribuire

[English](#contributing)

Grazie per l'aiuto nel mantenere **Open Medical Informatics** corretto e aggiornato. Ogni proposta viene rivista prima di essere accolta. Il curriculum sta in [README.it.md](README.it.md) (italiano) e [README.md](README.md) (inglese): i due file devono contenere sempre gli stessi corsi, nello stesso ordine.

## Criteri per le fonti

**Ammesse**
- Università, anche italiane (per esempio Federica Web Learning, EduOpen).
- Enti di standardizzazione: HL7, DICOM/NEMA, SNOMED International, Regenstrief/LOINC, OMS/ICD, OHDSI.
- Istituzioni: OMS, Commissione e Parlamento europeo, Ministero della Salute, ISS, AGENAS, AgID, Garante per la protezione dei dati personali.
- Letteratura peer-reviewed (PubMed/PMC, EQUATOR Network).
- Società scientifiche: AMIA, IMIA, EFMI.
- Organizzazioni non accademiche riconosciute (per esempio DeepLearning.AI, fast.ai, Google ML Crash Course, Kaggle Learn, Microsoft Learn, Hugging Face): sono etichettate **Industria** nella colonna «Tipo di fonte», e solo se i corsi sono gratuiti e di autori riconosciuti.

**Escluse**
- Blog e canali YouTube non istituzionali.
- Materiali di marketing dei fornitori.
- **Preprint** non revisionati: nessuna eccezione.
- Risorse a pagamento (master, certificazioni, libri). I corsi «in audit» sono ammessi solo se l'accesso gratuito è verificabile, e sono segnalati nelle Note.

## Che cosa deve contenere ogni voce

1. **Autore o ente** responsabile della risorsa.
2. **Link**. La data di verifica non si ripete in ogni voce: chi verifica i link aggiorna la data unica in testa ai README («Link verificati il»), dopo aver aperto ogni link e controllato che la risorsa sia gratuita e ancora disponibile.
3. **Tipo di fonte**: Università, Ente di standard, Istituzione, Peer-reviewed, Società scientifica oppure Industria.
4. **Citazione numerata in Bibliografia** in **stile Vancouver**, in ordine di prima comparsa, con DOI e/o PMID per gli articoli e gli estremi completi (titolo, numero, data, riferimento alla Gazzetta Ufficiale) per le norme. Ogni affermazione di fatto del curriculum (norme, cifre, definizioni) deve rinviare a una voce numerata.
5. Le solite colonne: lingua, impegno (con «stima» quando non lo dichiara la fonte), prerequisiti, note.

I nomi dei corsi, i titoli in Bibliografia e le norme restano nella forma originale (lingua e testo); si traduce solo il nostro testo descrittivo.

## Come proporre una voce o una correzione

- **Issue:** apri una issue con il link, il livello o l'indirizzo in cui la risorsa starebbe, il tipo di fonte e perché rispetta i criteri qui sopra. Le issue servono anche per segnalare un link rotto o datato, una cifra sbagliata o una nuova revisione di una norma.
- **Pull request:** modifica sia [README.it.md](README.it.md) sia [README.md](README.md) (stesso corso, stessa posizione, stessi numeri di citazione), aggiungi la voce Vancouver al posto giusto della Bibliografia rinumerando le successive, e descrivi la modifica.
- Le proposte che non rispettano i criteri vengono chiuse con una breve spiegazione.
- Non pubblicare dati di pazienti da nessuna parte: né nel repository, né nelle issue.

Dopo una modifica ai README, le pagine del sito si rigenerano con `python tools/genera_pagine.py`.

## Calendario delle revisioni

- **Link:** controllo automatico ogni mese (GitHub Actions, workflow «Link check», che apre una issue se trova link rotti). Le pagine che bloccano i bot (per esempio eur-lex.europa.eu) sono escluse e controllate a mano.
- **Contenuti:** revisione completa una volta all'anno; la data «Revisione» in cima ai README si aggiorna quando è fatta.
