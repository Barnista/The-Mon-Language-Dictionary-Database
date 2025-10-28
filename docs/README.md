The Mon Language — sql.js demo

This folder contains a small documentation/demo page that shows how to manage a SQLite database in the browser using sql.js (SQLite compiled to WebAssembly).

Files:
- index.html           — Documentation + interactive UI
- sqljs-demo.js        — Demo logic: init DB, create schema, insert sample rows, run arbitrary SQL, export DB
- app.js               — Existing project demo (left untouched)

Quick start
1. Serving over HTTP (recommended):
   - In PowerShell (from this repository root or the `dist` folder):
     python -m http.server 8000
   - Then open http://localhost:8000/dist/ in your browser.

2. Opening via file:// may fail in some browsers due to WASM/fetch restrictions. Use the local server above if you see errors loading the WebAssembly module.

How to use the page
- Click "Init DB (fresh)" to create an in-memory SQLite database.
- Click "Create Word schema" to create simple `Author` and `Word` tables compatible with the project's schema.
- Click "Insert sample rows" to populate a few rows (Thai, Burmese, Mon examples provided).
- Edit SQL in the textarea and click "Run SQL" to execute and render results.
- Click "Export DB" to download the current database as `themon.sqlite`.

Notes & tips
- The demo uses sql.js v1.8.0 from jsDelivr. You may change the CDN URL in `index.html` if you want a different version.
- The exported `.sqlite` file can be opened with desktop SQLite tools.
- Because this runs entirely in-browser (wasm), no server-side code is required.

If you want, I can also:
- Provide examples to import an existing `.sqlite` file into the demo page.
- Add more UI for CRUD operations on `Definition`, `Category`, etc.
