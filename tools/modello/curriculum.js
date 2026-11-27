/* Open Health Informatics: avanzamento dei corsi (caselle, barre, esporta, importa).
   JavaScript puro. Lo stato sta in localStorage con la stessa chiave nelle due lingue;
   ogni accesso e' in try/catch, e senza localStorage si lavora in memoria.
   Sorgente: tools/modello/curriculum.js nel repository open-health-informatics. */
(function () {
  'use strict';

  var cfg = { key: 'omi-progress-v1', lang: 'it', msg: {} };
  try {
    var el = document.getElementById('omi-config');
    if (el) { cfg = JSON.parse(el.textContent); }
  } catch (e) { /* si usano i valori di default */ }
  var KEY = cfg.key || 'omi-progress-v1';
  var M = cfg.msg || {};

  var boxes = [].slice.call(document.querySelectorAll('input.chk'));
  var byId = Object.create(null);
  boxes.forEach(function (b) { byId[b.getAttribute('data-id')] = b; });
  var bars = [].slice.call(document.querySelectorAll('.bar'));
  var statusEl = document.getElementById('omi-status');

  var memory = [];          // copia in memoria (unica copia se localStorage non funziona)
  var storageWarned = false;

  function say(text) {
    if (statusEl) { statusEl.textContent = text || ''; }
  }

  function fmt(template, vars) {
    return String(template || '').replace(/\{(\w+)\}/g, function (_, k) {
      return vars && vars[k] !== undefined ? vars[k] : '';
    });
  }

  function warnStorage() {
    if (!storageWarned) {
      storageWarned = true;
      say(M.storage_unavailable || '');
    }
  }

  function cleanList(list) {
    var seen = Object.create(null);
    var out = [];
    if (!Array.isArray(list)) { return out; }
    list.forEach(function (id) {
      if (typeof id === 'string' && byId[id] && !seen[id]) { seen[id] = true; out.push(id); }
    });
    return out;
  }

  function readStore() {
    var raw;
    try {
      raw = window.localStorage.getItem(KEY);
    } catch (e) {
      warnStorage();                 // storage non disponibile
      return memory.slice();
    }
    if (raw === null) { return memory.slice(); }
    var list;
    try {
      var data = JSON.parse(raw);
      list = Array.isArray(data) ? data : (data && data.done);
      if (!Array.isArray(list)) { throw new Error('format'); }
    } catch (e2) {
      say(M.storage_corrupt || '');  // dati presenti ma non leggibili: si riparte da zero
      memory = [];
      return [];
    }
    return cleanList(list);
  }

  function writeStore(list) {
    memory = list.slice();
    try {
      window.localStorage.setItem(KEY, JSON.stringify({ v: 1, done: list }));
    } catch (e) {
      warnStorage();
    }
  }

  function checkedIds() {
    return boxes.filter(function (b) { return b.checked; }).map(function (b) { return b.getAttribute('data-id'); });
  }

  function updateBars() {
    bars.forEach(function (bar) {
      var groups = (bar.getAttribute('data-groups') || '').split(/\s+/);
      var total = 0;
      var done = 0;
      boxes.forEach(function (b) {
        if (b.hasAttribute('data-optional')) { return; }
        if (groups.indexOf(b.getAttribute('data-group')) === -1) { return; }
        total += 1;
        if (b.checked) { done += 1; }
      });
      var pct = total ? Math.round(done * 100 / total) : 0;
      var fill = bar.querySelector('.bar-fill');
      var num = bar.querySelector('.bar-num');
      var track = bar.querySelector('.bar-track');
      if (fill) { fill.style.width = pct + '%'; }
      if (num) { num.textContent = done + ' / ' + total + ' (' + pct + '%)'; }
      if (track) {
        track.setAttribute('aria-valuemax', String(total));
        track.setAttribute('aria-valuenow', String(done));
      }
    });
  }

  function paintCards() {
    boxes.forEach(function (b) {
      var card = b.closest ? b.closest('.corso') : null;
      if (card) { card.classList.toggle('fatto', b.checked); }
    });
  }

  function applyList(list) {
    var on = Object.create(null);
    list.forEach(function (id) { on[id] = true; });
    boxes.forEach(function (b) { b.checked = !!on[b.getAttribute('data-id')]; });
    paintCards();
    updateBars();
  }

  function onChange() {
    writeStore(checkedIds());
    paintCards();
    updateBars();
  }

  boxes.forEach(function (b) { b.addEventListener('change', onChange); });

  /* Esporta */
  var btnExport = document.getElementById('omi-export');
  if (btnExport) {
    btnExport.addEventListener('click', function () {
      try {
        var data = {
          app: 'open-health-informatics',
          version: 1,
          exported: new Date().toISOString(),
          done: checkedIds()
        };
        var blob = new Blob([JSON.stringify(data, null, 2) + '\n'], { type: 'application/json' });
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'open-health-informatics-progress.json';
        a.style.display = 'none';
        document.body.appendChild(a);
        a.click();
        setTimeout(function () {
          if (a.parentNode) { a.parentNode.removeChild(a); }
          URL.revokeObjectURL(url);
        }, 30000);
        say(M.exported);
      } catch (e) {
        say(M.export_error);
      }
    });
  }

  /* Importa */
  var btnImport = document.getElementById('omi-import');
  var fileInput = document.getElementById('omi-file');
  if (btnImport && fileInput) {
    btnImport.addEventListener('click', function () { fileInput.click(); });
    fileInput.addEventListener('change', function () {
      var file = fileInput.files && fileInput.files[0];
      if (!file) { return; }
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var data = JSON.parse(String(reader.result));
          var list = Array.isArray(data) ? data : (data && data.done);
          if (!Array.isArray(list)) { throw new Error('format'); }
          var known = cleanList(list);
          var unknown = list.length - known.length;
          applyList(known);
          writeStore(known);
          say(fmt(unknown > 0 ? M.imported_unknown : M.imported, { n: known.length, u: unknown }));
        } catch (e) {
          say(M.import_error);
        }
        try { fileInput.value = ''; } catch (e2) { /* niente */ }
      };
      reader.onerror = function () { say(M.import_error); };
      reader.readAsText(file);
    });
  }

  /* Azzera */
  var btnReset = document.getElementById('omi-reset');
  if (btnReset) {
    btnReset.addEventListener('click', function () {
      var ok = true;
      try { ok = window.confirm(M.reset_confirm || ''); } catch (e) { ok = true; }
      if (!ok) { return; }
      applyList([]);
      writeStore([]);
      say(M.reset_done);
    });
  }

  /* Sincronizza con le altre schede aperte (per esempio l'altra lingua) */
  window.addEventListener('storage', function (e) {
    if (e.key === null) {            // storage svuotato da un'altra scheda
      memory = [];
      applyList([]);
    } else if (e.key === KEY) {
      applyList(e.newValue === null ? [] : readStore());
      if (e.newValue === null) { memory = []; }
    }
  });
  window.addEventListener('pageshow', function (e) {
    if (e.persisted) { applyList(readStore()); }
  });

  applyList(readStore());
})();
