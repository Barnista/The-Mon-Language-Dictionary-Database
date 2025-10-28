from pathlib import Path
import re
import sys
import time

#!/usr/bin/env python3
"""
Read ../sql/data/definitions.sql and split out each INSERT INTO ...; statement
into its own JavaScript file. Each JS file contains a single string variable
holding the INSERT statement and exports it (CommonJS).
"""

# Paths (relative to this script)
HERE = Path(__file__).parent.resolve()
SRC_Author = (HERE / "../sql/data/Author.sql").resolve()
SRC_Category = (HERE / "../sql/data/Category.sql").resolve()
SRC_CategoryDetail = (HERE / "../sql/data/CategoryDetail.sql").resolve()
SRC_Definition = (HERE / "../sql/data/Definition.sql").resolve()
SRC_Word = (HERE / "../sql/data/Word.sql").resolve()
OUT_DIR = (HERE / "../dist/assets/database").resolve()
OUT_DIR.mkdir(parents=True, exist_ok=True)

def build_sql_js(sql):
    # Find all INSERT ... ; sequences (non-greedy, DOTALL to span lines)
    pattern = re.compile(r'(INSERT\s+INTO\b.*?;)', re.IGNORECASE | re.DOTALL)
    matches = pattern.findall(sql)
    if not matches:
        print("No INSERT statements found.", file=sys.stderr)
        sys.exit(1)
    # Helper to get a safe filename from the table name
    def sanitize_table_name(raw):
        # remove backticks, quotes and replace dots with underscores
        s = raw.replace("`", "").replace('"', "").replace("'", "")
        s = s.replace(".", "_")
        # keep alnum and underscores, replace others with underscore
        s = re.sub(r'[^A-Za-z0-9_]', '_', s)
        return s.lower()
    # Extract table name for naming, and write files
    table_counts = {}
    for idx, stmt in enumerate(matches, start=1):
        # Try to capture the table name after INSERT INTO
        #m = stmt.replace(";", "")
        m = re.match(r'INSERT\s+INTO\s+((?:`?[\w$]+`?(?:\.`?[\w$]+`?)?))', stmt, re.IGNORECASE)
        if m:
            raw_table = m.group(1)
            name = sanitize_table_name(raw_table)
        else:
            name = f"unknown_{idx}"

        # ensure unique filename
        count = table_counts.get(name, 0) + 1
        table_counts[name] = count
        #filename = f"{idx:03d}_{name}"
        filename = f"{name}"
        if count > 0:
            filename = f"{filename}_{count}"
        filename = OUT_DIR / (filename + ".js")

        # Data cleansing to avoid causing bugs on sql.js
        # By removing ` and replacing \'s
        value = stmt.replace("`", "")
        value = value.replace("\\'", "’")
        value = value.strip()
        # Prepare JS content: const sql = `...`; module.exports = sql;
        #js_content = f"const DB_DATA_{name.upper()}_{count} = `\n" + value + "\n`;\n\nmodule.exports = sql;\n"
        js_content = f"const DB_DATA_{name.upper()}_{count} = `\n" + value + "\n`;\n"

        filename.write_text(js_content, encoding="utf-8")
    print(f"Wrote {len(matches)} files to: {OUT_DIR}")


if not SRC_Author.exists():
    print(f"Source SQL file not found: {SRC_Author}", file=sys.stderr)
    sys.exit(1)
else:
    text = SRC_Author.read_text(encoding="utf-8")
    build_sql_js(text)

if not SRC_Category.exists():
    print(f"Source SQL file not found: {SRC_Category}", file=sys.stderr)
    sys.exit(1)
else:
    text = SRC_Category.read_text(encoding="utf-8")
    build_sql_js(text)

if not SRC_CategoryDetail.exists():
    print(f"Source SQL file not found: {SRC_CategoryDetail}", file=sys.stderr)
    sys.exit(1)
else:
    text = SRC_CategoryDetail.read_text(encoding="utf-8")
    build_sql_js(text)

if not SRC_Definition.exists():
    print(f"Source SQL file not found: {SRC_Definition}", file=sys.stderr)
    sys.exit(1)
else:
    text = SRC_Definition.read_text(encoding="utf-8")
    build_sql_js(text)

if not SRC_Word.exists():
    print(f"Source SQL file not found: {SRC_Word}", file=sys.stderr)
    sys.exit(1)
else:
    text = SRC_Word.read_text(encoding="utf-8")
    build_sql_js(text)