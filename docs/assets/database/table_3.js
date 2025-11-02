const DB_TABLES_3 = `
CREATE TABLE Category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_category_id INTEGER,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER
);
`;
