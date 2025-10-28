(async function(){
  // initSqlJs is provided by sql-wasm.js loaded in index.html
  const SQL = await initSqlJs(window.initSqlJsConfig || {});
  let db = null;

  const outputEl = document.getElementById('output');
  function setOutput(html){ outputEl.innerHTML = html; }
  function showError(err){ setOutput(`<pre style="color:firebrick">${String(err)}</pre>`); }

  function escapeHtml(s){
    return String(s)
      .replace(/&/g,'&amp;')
      .replace(/</g,'&lt;')
      .replace(/>/g,'&gt;');
  }

  function initDb(){
    if(db){ db.close(); }
    db = new SQL.Database();
    setOutput('<pre>Initialized new in-memory database.</pre>');
  }

  function createWordSchema(){
    const sql = `
CREATE TABLE IF NOT EXISTS Author (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Word (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  synonym_word_id INTEGER,
  word TEXT NOT NULL,
  ipa TEXT,
  th TEXT,
  lang_code TEXT(3) NOT NULL,
  created_at DATETIME DEFAULT (datetime('now')),
  author_id INTEGER,
  FOREIGN KEY (synonym_word_id) REFERENCES Word(id),
  FOREIGN KEY (author_id) REFERENCES Author(id)
);
`;
    try{
      db.exec("PRAGMA foreign_keys = ON;");
      db.exec(sql);
      setOutput('<pre>Created Author and Word tables.</pre>');
    }catch(e){ showError(e); }
  }

  function insertSampleRows(){
    try{
      const insertAuthor = db.prepare('INSERT INTO Author (name) VALUES (?);');
      db.exec('BEGIN;');
      insertAuthor.run(['Default Author']);
      insertAuthor.free();

      const insert = db.prepare('INSERT INTO Word (word, ipa, th, lang_code, author_id, synonym_word_id) VALUES (?, ?, ?, ?, ?, ?);');
      const samples = [
        ['မင်္ဂလာပါ','mɪ̀ɴɡəlà bà','สวัสดี','my',1,null],
        ['สวัสดี','sa-wat-dee',null,'th',1,null],
        ['မော်နား','mɔ̀ná',null,'mn',1,null]
      ];
      for(const r of samples){ insert.run(r); }
      insert.free();
      db.exec('COMMIT;');
      setOutput('<pre>Inserted '+samples.length+' sample rows into Word.</pre>');
    }catch(e){ db.exec('ROLLBACK;'); showError(e); }
  }

  function runSQL(showFirstOnly){
    const sql = document.getElementById('sql-input').value;
    try{
      const results = db.exec(sql);
      if(!results || results.length===0){ setOutput('<pre>No results returned.</pre>'); return; }
      const res = results[0];
      const cols = res.columns;
      const rows = res.values;
      if(showFirstOnly){
        const first = rows[0] || [];
        let out = '<table><thead><tr>'+cols.map(c=>`<th>${escapeHtml(c)}</th>`).join('')+'</tr></thead><tbody>';
        out += '<tr>'+first.map(v=>`<td>${escapeHtml(v===null? 'NULL': v)}</td>`).join('')+'</tr>';
        out += '</tbody></table>';
        setOutput(out);
        return;
      }
      let out = '<table><thead><tr>'+cols.map(c=>`<th>${escapeHtml(c)}</th>`).join('')+'</tr></thead><tbody>';
      for(const r of rows){ out += '<tr>'+r.map(v=>`<td>${escapeHtml(v===null? 'NULL': v)}</td>`).join('')+'</tr>'; }
      out += '</tbody></table>';
      setOutput(out);
    }catch(e){ showError(e); }
  }

  function exportDB(){
    try{
      const data = db.export(); // Uint8Array
      const blob = new Blob([data], {type: 'application/x-sqlite3'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = 'themon.sqlite'; a.click();
      URL.revokeObjectURL(url);
      setOutput('<pre>Exported themon.sqlite</pre>');
    }catch(e){ showError(e); }
  }

  // Wire UI
  document.getElementById('btn-init').addEventListener('click', ()=>initDb());
  document.getElementById('btn-create-schema').addEventListener('click', ()=>{
    if(!db) return showError('DB not initialized. Click Init DB first.');
    createWordSchema();
  });
  document.getElementById('btn-insert-sample').addEventListener('click', ()=>{
    if(!db) return showError('DB not initialized. Click Init DB first.');
    insertSampleRows();
  });
  document.getElementById('btn-run').addEventListener('click', ()=>{
    if(!db) return showError('DB not initialized. Click Init DB first.');
    runSQL(false);
  });
  document.getElementById('btn-run-select').addEventListener('click', ()=>{
    if(!db) return showError('DB not initialized. Click Init DB first.');
    runSQL(true);
  });
  document.getElementById('btn-export').addEventListener('click', ()=>{
    if(!db) return showError('DB not initialized. Click Init DB first.');
    exportDB();
  });
  document.getElementById('btn-clear').addEventListener('click', ()=>setOutput(''));

  // Auto init
  initDb();

})();
