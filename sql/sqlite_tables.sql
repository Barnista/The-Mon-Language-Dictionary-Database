-- SQLite doesn't support CREATE DATABASE, it's file-based
-- Just start with table creation

CREATE TABLE Author (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT
);

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

CREATE TABLE Category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_category_id INTEGER,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER
);

CREATE TABLE CategoryDetail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    label TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER,
    lang_code TEXT
);

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
