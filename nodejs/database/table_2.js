export const DB_TABLES_2 = `
CREATE TABLE Word (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    synonym_word_id INTEGER,
    word TEXT NOT NULL,
    ipa TEXT,
    th TEXT,
    lang_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER
);
`;
