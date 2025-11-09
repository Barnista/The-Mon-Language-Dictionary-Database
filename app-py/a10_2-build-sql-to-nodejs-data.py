from pathlib import Path
import re
import sys
import time

#!/usr/bin/env python3
"""
Read ../sql/definitions.sql and split out each INSERT INTO ...; statement
into its own JavaScript file. Each JS file contains a single string variable
holding the INSERT statement and exports it (CommonJS).
"""

# Paths (relative to this script)
HERE = Path(__file__).parent.resolve()
SRC_Author = (HERE / "../sql/Author.sql").resolve()
SRC_Category = (HERE / "../sql/Category.sql").resolve()
SRC_CategoryDetail = (HERE / "../sql/CategoryDetail.sql").resolve()
SRC_Definition = (HERE / "../sql/Definition.sql").resolve()
SRC_Word = (HERE / "../sql/Word.sql").resolve()
SRC_TABLES = (HERE / "../sql/sqlite_tables.sql").resolve()
OUT_DIR = (HERE / "../nodejs/data").resolve()
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_DIR_TABLE = (HERE / "../nodejs/table").resolve()
OUT_DIR_TABLE.mkdir(parents=True, exist_ok=True)
OUT_DIR_ROOT = (HERE / "../nodejs").resolve()
OUT_DIR_TABLE.mkdir(parents=True, exist_ok=True)

def partition_lines(lines, size):
    parts = list()
    if size >= 7800:
        # 7 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:3600])
        parts.append(lines[3600:4200])
        parts.append(lines[4200:4800])
        parts.append(lines[4800:5400])
        parts.append(lines[5400:6000])
        parts.append(lines[6000:6600])
        parts.append(lines[6600:7200])
        parts.append(lines[7200:7800])
        parts.append(lines[7800:])
    elif size >= 7200:
        # 7 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:3600])
        parts.append(lines[3600:4200])
        parts.append(lines[4200:4800])
        parts.append(lines[4800:5400])
        parts.append(lines[5400:6000])
        parts.append(lines[6000:6600])
        parts.append(lines[6600:7200])
        parts.append(lines[7200:])
    elif size >= 6600:
        # 7 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:3600])
        parts.append(lines[3600:4200])
        parts.append(lines[4200:4800])
        parts.append(lines[4800:5400])
        parts.append(lines[5400:6000])
        parts.append(lines[6000:6600])
        parts.append(lines[6600:])
    elif size >= 6000:
        # 7 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:3600])
        parts.append(lines[3600:4200])
        parts.append(lines[4200:4800])
        parts.append(lines[4800:5400])
        parts.append(lines[5400:6000])
        parts.append(lines[6000:])
    elif size >= 5400:
        # 7 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:3600])
        parts.append(lines[3600:4200])
        parts.append(lines[4200:4800])
        parts.append(lines[4800:5400])
        parts.append(lines[5400:])
    elif size >= 4800:
        # 7 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:3600])
        parts.append(lines[3600:4200])
        parts.append(lines[4200:4800])
        parts.append(lines[4800:])
    elif size >= 4200:
        # 7 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:3600])
        parts.append(lines[3600:4200])
        parts.append(lines[4200:])
    elif size >= 3600:
        # 7 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:3600])
        parts.append(lines[3600:])
    elif size >= 3000:
        # 6 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:3000])
        parts.append(lines[3000:])
    elif size >= 2400:
        # 5 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:2400])
        parts.append(lines[2400:])
    elif size >= 1800:
        # 4 parts
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:1800])
        parts.append(lines[1800:])
    elif size >= 1200:
        parts.append(lines[1:600])
        parts.append(lines[600:1200])
        parts.append(lines[1200:])
        # 3 parts
    elif size >= 600:
        parts.append(lines[1:600])
        parts.append(lines[600:])
        # 2 parts
    else:
        parts.append(lines[1:])
        # 1 part
    return parts

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

        # Data cleansing to avoid causing bugs on sql.js
        # By removing ` and replacing \'s
        value = stmt.replace("`", "")
        value = value.replace("\\'", "’")
        value = value.strip()

        #Optiomize the value down from 1mb to 250kb by partitioning
        lines = value.split('\n')
        sql_command = lines[0]
        size = len(lines)
        parts = partition_lines(lines, size)

        for i, pt in enumerate(parts):
            # Prepare JS content
            value = sql_command + '\n'
            value = value + "\n".join(pt)

            #if the last char of this value is "," then remove it
            if value.strip().endswith(','):
                value = value.rstrip().rstrip(',')

            # ensure unique filename
            count = table_counts.get(name, 0) + 1
            table_counts[name] = count
            #filename = f"{idx:03d}_{name}"
            filename = f"{name}"
            if count > 0:
                filename = f"{filename}_{count}"
            filename = OUT_DIR / (filename + ".js")

            js_content = f"/* eslint-disable no-useless-escape */ \nexport const DB_DATA_{name.upper()}_{count} = `" + value + "`;\n /* eslint-disable no-useless-escape */"
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

def build_table_js(sql):
    # Find all CREATE TABLE statements (non-greedy, DOTALL to span lines)
    pattern = re.compile(r'(CREATE\s+TABLE\b.*?;)', re.IGNORECASE | re.DOTALL)
    matches = pattern.findall(sql)
    if not matches:
        print("No CREATE TABLE statements found.", file=sys.stderr)
        sys.exit(1)
    # Extract table name and write file
    for index, stmt in enumerate(matches):
        # Clean up statement
        value = stmt.replace("`", "")
        value = value.replace("\\'", "'")
        value = value.replace("\n", "")
        value = value.strip()
        
        # Write to single file
        js_content = f"/* eslint-disable no-useless-escape */ export const DB_TABLES_{index+1} = `" + value + "`; /* eslint-disable no-useless-escape */"
        table_file = OUT_DIR_TABLE / f"table_{index+1}.js"
        table_file.write_text(js_content, encoding="utf-8")

if not SRC_TABLES.exists():
    print(f"Source SQL tables file not found: {SRC_TABLES}", file=sys.stderr)
    sys.exit(1)
else:
    text = SRC_TABLES.read_text(encoding="utf-8")
    build_table_js(text)


