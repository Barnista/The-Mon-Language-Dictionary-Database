CREATE DATABASE IF NOT EXISTS TheMonLanguageDictionary
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
USE TheMonLanguageDictionary;

CREATE TABLE Author (
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- Add other columns for Author as needed
    name VARCHAR(255) NOT NULL,
    bio TEXT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE Word (
    id INT AUTO_INCREMENT PRIMARY KEY,
    synonym_word_id INT,
    word VARCHAR(200) NOT NULL,
    ipa VARCHAR(1000) NULL,
    th VARCHAR(1000) NULL,
    lang_code VARCHAR(3) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Table: Category
CREATE TABLE Category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parent_category_id INT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Table: CategoryDetail
CREATE TABLE CategoryDetail (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    label VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT NULL,
    lang_code VARCHAR(3)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Table: Definition
CREATE TABLE Definition (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word_id INT NOT NULL,
    lang_code VARCHAR(3) NOT NULL,
    pos_code VARCHAR(10) NOT NULL,
    category_id INT NULL,
    definition TEXT NOT NULL,
    example TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

