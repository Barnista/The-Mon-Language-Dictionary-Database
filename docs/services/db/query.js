const DB_QUERY = {
    Author: {
        tableName: 'Author',
        selectAll: (db) => {
            const q = `SELECT * FROM ${DB_QUERY.Author.tableName}`;
            return {
                query: q,
                exec: () => {
                    // Prepare a statement
                    const result = db.exec(q);
                    if (result[0]) result[0];
                    return result;
                }
            }
        },
        select: (db, id) => {
            const q = `SELECT * FROM ${DB_QUERY.Author.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return result[0];
                    return result;
                }
            }
        },
        create: (db, name, bio) => {
            const q = `INSERT INTO ${DB_QUERY.Author.tableName} VALUES (NULL, '${name}', '${bio}')`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    return result;
                }
            }
        },
        update: (db, id, name, bio) => {
            const q = `UPDATE ${DB_QUERY.Author.tableName} SET name = '${name}', bio = '${bio}' WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        delete: (db, id) => {
            const q = `DELETE FROM ${DB_QUERY.Author.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        count: (db) => {
            // Prepare a statement
            const q = `SELECT COUNT(*) FROM ${DB_QUERY.Author.tableName}`
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return {
                        query: q,
                        result: result[0].values[0][0]
                    };
                    return {
                        query: q,
                        result: result
                    };
                }
            }
        },
    },
    Category: {
        tableName: 'Category',
        selectAll: (db) => {
            const q = `SELECT * FROM ${DB_QUERY.Category.tableName}`;
            return {
                query: q,
                exec: () => {
                    // Prepare a statement
                    const result = db.exec(q);
                    if (result[0]) result[0];
                    return result;
                }
            }
        },
        select: (db, id) => {
            const q = `SELECT * FROM ${DB_QUERY.Category.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return result[0];
                    return result;
                }
            }
        },
        create: (db, name, bio) => {
            const q = `INSERT INTO ${DB_QUERY.Category.tableName} VALUES (NULL, '${name}', '${bio}')`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    return result;
                }
            }
        },
        update: (db, id, name, bio) => {
            const q = `UPDATE ${DB_QUERY.Category.tableName} SET name = '${name}', bio = '${bio}' WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        delete: (db, id) => {
            const q = `DELETE FROM ${DB_QUERY.Category.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        count: (db) => {
            // Prepare a statement
            const q = `SELECT COUNT(*) FROM ${DB_QUERY.Category.tableName}`
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return {
                        query: q,
                        result: result[0].values[0][0]
                    };
                    return {
                        query: q,
                        result: result
                    };
                }
            }
        },
    },
    CategoryDetail: {
        tableName: 'CategoryDetail',
        selectAll: (db) => {
            const q = `SELECT * FROM ${DB_QUERY.CategoryDetail.tableName}`;
            return {
                query: q,
                exec: () => {
                    // Prepare a statement
                    const result = db.exec(q);
                    if (result[0]) result[0];
                    return result;
                }
            }
        },
        select: (db, id) => {
            const q = `SELECT * FROM ${DB_QUERY.CategoryDetail.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return result[0];
                    return result;
                }
            }
        },
        create: (db, name, bio) => {
            const q = `INSERT INTO ${DB_QUERY.CategoryDetail.tableName} VALUES (NULL, '${name}', '${bio}')`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    return result;
                }
            }
        },
        update: (db, id, name, bio) => {
            const q = `UPDATE ${DB_QUERY.CategoryDetail.tableName} SET name = '${name}', bio = '${bio}' WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        delete: (db, id) => {
            const q = `DELETE FROM ${DB_QUERY.CategoryDetail.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        count: (db) => {
            // Prepare a statement
            const q = `SELECT COUNT(*) FROM ${DB_QUERY.CategoryDetail.tableName}`
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return {
                        query: q,
                        result: result[0].values[0][0]
                    };
                    return {
                        query: q,
                        result: result
                    };
                }
            }
        },
    },
    Word: {
        tableName: 'Word',
        selectAll: (db) => {
            const q = `SELECT * FROM ${DB_QUERY.Word.tableName}`;
            return {
                query: q,
                exec: () => {
                    // Prepare a statement
                    const result = db.exec(q);
                    if (result[0]) result[0];
                    return result;
                }
            }
        },
        select: (db, id) => {
            const q = `SELECT * FROM ${DB_QUERY.Word.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return result[0];
                    return result;
                }
            }
        },
        create: (db, name, bio) => {
            const q = `INSERT INTO ${DB_QUERY.Word.tableName} VALUES (NULL, '${name}', '${bio}')`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    return result;
                }
            }
        },
        update: (db, id, name, bio) => {
            const q = `UPDATE ${DB_QUERY.Word.tableName} SET name = '${name}', bio = '${bio}' WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        delete: (db, id) => {
            const q = `DELETE FROM ${DB_QUERY.Word.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        count: (db) => {
            // Prepare a statement
            const q = `SELECT COUNT(*) FROM ${DB_QUERY.Word.tableName}`
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return {
                        query: q,
                        result: result[0].values[0][0]
                    };
                    return {
                        query: q,
                        result: result
                    };
                }
            }
        },
    },
    Definition: {
        tableName: 'Definition',
        selectAll: (db) => {
            const q = `SELECT * FROM ${DB_QUERY.Definition.tableName}`;
            return {
                query: q,
                exec: () => {
                    // Prepare a statement
                    const result = db.exec(q);
                    if (result[0]) result[0];
                    return result;
                }
            }
        },
        select: (db, id) => {
            const q = `SELECT * FROM ${DB_QUERY.Definition.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return result[0];
                    return result;
                }
            }
        },
        create: (db, name, bio) => {
            const q = `INSERT INTO ${DB_QUERY.Definition.tableName} VALUES (NULL, '${name}', '${bio}')`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    return result;
                }
            }
        },
        update: (db, id, name, bio) => {
            const q = `UPDATE ${DB_QUERY.Definition.tableName} SET name = '${name}', bio = '${bio}' WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        delete: (db, id) => {
            const q = `DELETE FROM ${DB_QUERY.Definition.tableName} WHERE id = ${id}`;
            return {
                query: q,
                exec: () => {
                    const result = db.exec(query);
                    return result;
                }
            }
        },
        count: (db) => {
            // Prepare a statement
            const q = `SELECT COUNT(*) FROM ${DB_QUERY.Definition.tableName}`
            return {
                query: q,
                exec: () => {
                    const result = db.exec(q);
                    if (result[0]) return {
                        query: q,
                        result: result[0].values[0][0]
                    };
                    return {
                        query: q,
                        result: result
                    };
                }
            }
        },
    },
}

const DB_QUERY_PRESET = {
    SELECT_ALL: `SELECT * FROM {table} LIMIT(1000);`,
    SELECT_WHERE: `SELECT * FROM {table} WHERE {condition} LIMIT(1000);`,
    SELECT_COUNT: `SELECT COUNT(*) FROM {table};`,
    SELECT_DISTINCT: `SELECT DISTINCT {column} FROM {table};`,
    INSERT_INTO: `INSERT INTO {table} ({column1}, {column2}, {column3}) VALUES ({value1}, {value2}, {value3});`,
    UPDATE: `UPDATE {table} SET {column1} = {value1}, {column2} = {value2} WHERE {condition};`,
    DELETE: `DELETE FROM {table} WHERE {condition};`
}

const DB_QUERY_INSTANTS = {
    SELECT_Word_JOIN_Definition_JOIN_Author: `
        SELECT 
            Word.word as 'Mon Word',
            Word.ipa as 'IPA',
            Word.th as 'TH',
            Definition.definition as 'Definition',
            Definition.lang_code as 'Language',
            Definition.pos_code as 'Part of Speech',
            Author.name as 'Author'
        FROM 
            Word
        JOIN 
            Definition ON Word.id = Definition.word_id
        JOIN 
            Author ON Definition.author_id = Author.id
        WHERE 
            Word.word LIKE '%တ္ၚဲ%'
        ORDER BY
            Word.word
        LIMIT 1000;`,
    SELECT_Word_JOIN_Definition_WHERE_Definition: `
        SELECT 
            Word.word as 'Mon Word',
            Word.ipa as 'IPA',
            Word.th as 'TH',
            Definition.definition as 'Definition',
            Definition.lang_code as 'Language',
            Definition.pos_code as 'Part of Speech',
            Author.name as 'Author'
        FROM 
            Word
        JOIN 
            Definition ON Word.id = Definition.word_id
        JOIN 
            Author ON Definition.author_id = Author.id
        WHERE 
            Definition.definition LIKE '%rice%' OR
            Definition.definition LIKE '%ข้าว%' OR
            Definition.definition LIKE '%ထမင်း%'
        ORDER BY
            Word.word ASC
        LIMIT 1000;
    `,
    SELECT_Word_JOIN_Word_WHERE_Synonym: `
        SELECT 
            W1.word as 'Word (Main)',
            W2.word as 'Word (Synonym)',
            W1.ipa as 'IPA (Main)',
            W1.th as 'TH (Main)',
            W2.ipa as 'IPA (Synonym)',
            W2.th as 'TH (Synonym)'
        FROM 
            Word as W1
        JOIN 
            Word as W2 ON W1.synonym_word_id = W2.id
        WHERE 
            W1.synonym_word_id IS NOT NULL AND
            W1.th IS NOT NULL AND
            W2.th IS NOT NULL
        ORDER BY
            W2.word ASC
        LIMIT 1000;
    `,
    SELECT_Word_JOIN_Definition_WHERE_IS_Pronoun: `
        SELECT 
            Word.word as 'Mon Word',
            Word.ipa as 'IPA',
            Word.th as 'TH',
            Definition.definition as 'Definition',
            Definition.lang_code as 'Language',
            Definition.pos_code as 'Part of Speech',
            Author.name as 'Author'
        FROM 
            Word
        JOIN 
            Definition ON Word.id = Definition.word_id
        JOIN 
            Author ON Definition.author_id = Author.id
        WHERE 
            Definition.pos_code = 'pron'
        ORDER BY
            Word.word ASC
        LIMIT 1000;
    `,
    SELECT_Definition_JOIN_Category_WHERE: `
        SELECT 
            Category.name as 'Category',
            Word.word as 'Mon Word',
            Definition.definition as 'Definition',
            Definition.lang_code as 'Language',
            Definition.pos_code as 'Part of Speech',
            Author.name as 'Author'
        FROM 
            Definition
        JOIN 
            Word ON Word.id = Definition.word_id
        JOIN
            Category ON Category.id = Definition.category_id
        JOIN 
            Author ON Definition.author_id = Author.id
        WHERE 
            Definition.category_id IS NOT NULL AND
            Category.name LIKE '%Fruits%'
        ORDER BY
            Word.word ASC
        LIMIT 1000;
    `,
    SELECT_Definition_JOIN_Word_WHERE_Definition: `
        SELECT 
            Word.word as 'Mon Word',
            Word.ipa as 'IPA',
            Word.th as 'TH',
            Definition.definition as 'Definition',
            Definition.lang_code as 'Language',
            Definition.pos_code as 'Part of Speech',
            Author.name as 'Author'
        FROM 
            Definition
        JOIN 
            Word ON Word.id = Definition.word_id
        JOIN 
            Author ON Definition.author_id = Author.id
        WHERE 
            Definition.definition LIKE 'Ministry%'
        ORDER BY
            Word.word ASC
        LIMIT 1000;
    `,
    SELECT_Author_Summary: `
        SELECT 
            A1.name as 'Name',
            A1.bio as 'Bio',
            (SELECT COUNT(*) 
                FROM 
                    Word 
                JOIN 
                    Author ON Word.author_id = Author.id 
                WHERE 
                    Author.name LIKE CONCAT('%', A1.name, '%')
            ) as 'Word Compiled',
            (SELECT COUNT(*) 
                FROM 
                    Definition 
                JOIN 
                    Author ON Definition.author_id = Author.id 
                WHERE 
                    Author.name LIKE CONCAT('%', A1.name, '%')
            ) as 'Definition Compiled' 
        FROM
            Author as A1 
        WHERE
            A1.id = 1 OR A1.id = 2; 
    `
}