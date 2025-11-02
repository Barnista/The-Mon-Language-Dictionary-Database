export const DB_TABLES_5 = `
CREATE TABLE Definition (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    lang_code TEXT NOT NULL,
    pos_code TEXT NOT NULL,
    category_id INTEGER,
    definition TEXT NOT NULL,
    example TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER
);
`;
