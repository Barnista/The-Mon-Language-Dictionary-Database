const DB_QUERY = {
    Author: {
        selectAll: (db) => {
            // Prepare a statement
            const query = `SELECT * FROM Author`;
            const result = db.exec(query);
            if (result[0]) return {
                query: query,
                result: result[0]
            };
            return {
                query: query,
                result: result
            };
        },
        select: (db, id) => {
            const query = `SELECT * FROM Author WHERE id = ${id}`;
            const result = db.exec(query);
            if (result[0]) return {
                query: query,
                result: result[0]
            };
            return {
                query: query,
                result: result
            };
        },
        create: (db, name, bio) => {
            const query = `INSERT INTO Author VALUES (NULL, '${name}', '${bio}')`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        },
        update: (db, id, name, bio) => {
            const query = `UPDATE Author SET name = '${name}', bio = '${bio}' WHERE id = ${id}`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        },
        delete: (db, id) => {
            const query = `DELETE FROM Author WHERE id = ${id}`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        }
    },
    Category: {
        selectAll: (db) => {
            // Prepare a statement
            const query = `SELECT * FROM Category`;
            const result = db.exec(query);

            if (result[0]) return {
                query: query,
                result: result[0]
            };

            return {
                query: query,
                result: result
            };
        },
        select: (db, id) => {
            const query = `SELECT * FROM Category WHERE id = ${id}`;
            const result = db.exec(query);

            if (result[0]) return {
                query: query,
                result: result[0]
            };

            return {
                query: query,
                result: result
            };
        },
        create: (db, parent_category_id, name, author_id) => {
            const query = `INSERT INTO Category VALUES (NULL, ${parent_category_id}, '${name}', NOW(), ${author_id})`;
            const result = db.exec(query);

            return {
                query: query,
                result: result
            };
        },
        update: (db, id, parent_category_id, name, author_id) => {
            const query = `UPDATE Category SET parent_category_id = ${parent_category_id}, name = '${name}', created_at = NOW(), author_id = ${author_id} WHERE id = ${id}`;
            const result = db.exec(query);

            return {
                query: query,
                result: result
            };
        },
        delete: (db, id) => {
            const query = `DELETE FROM Category WHERE id = ${id}`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        }
    },
    CategoryDetail: {
        selectAll: (db) => {
            // Prepare a statement
            const query = `SELECT * FROM CategoryDetail`;
            const result = db.exec(query);

            if (result[0]) return {
                query: query,
                result: result[0]
            };

            return {
                query: query,
                result: result
            };
        },
        select: (db, id) => {
            const query = `SELECT * FROM CategoryDetail WHERE id = ${id}`;
            const result = db.exec(query);

            if (result[0]) return {
                query: query,
                result: result[0]
            };

            return {
                query: query,
                result: result
            };
        },
        create: (db, category_id, label, description, author_id, lang_code) => {
            const query = `INSERT INTO CategoryDetail VALUES (NULL, ${category_id}, '${label}', '${description}', NOW(), ${author_id}, '${lang_code}')`;
            const result = db.exec(query);

            return {
                query: query,
                result: result
            };
        },
        update: (db, id, category_id, label, description, author_id, lang_code) => {
            const query = `UPDATE CategoryDetail SET category_id = ${category_id}, label = '${label}', description = '${description}', author_id = ${author_id}, lang_code = '${lang_code}' WHERE id = ${id}`;
            const result = db.exec(query);

            return {
                query: query,
                result: result
            };
        },
        delete: (db, id) => {
            const query = `DELETE FROM CategoryDetail WHERE id = ${id}`;
            const result = db.exec(query);

            return {
                query: query,
                result: result
            };
        }
    },
    Word: {
        selectAll: (db) => {
            // Prepare a statement
            const query = `SELECT * FROM Word`;
            const result = db.exec(query);
            if (result[0]) return {
                query: query,
                result: result[0]
            };
            return {
                query: query,
                result: result
            };
        },
        select: (db, id) => {
            const query = `SELECT * FROM Word WHERE id = ${id}`;
            const result = db.exec(query);
            if (result[0]) return {
                query: query,
                result: result[0]
            };
            return {
                query: query,
                result: result
            };
        },
        create: (db, synonym_word_id, word, ipa, th, lang_code, author_id) => {
            const query = `INSERT INTO Word VALUES (NULL, ${synonym_word_id}, '${word}', '${ipa}', '${th}', '${lang_code}', NOW(), ${author_id})`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        },
        update: (db, id, synonym_word_id, word, ipa, th, lang_code, author_id) => {
            const query = `UPDATE Word SET synonym_word_id = ${synonym_word_id}, word = '${word}', ipa = '${ipa}', th = '${th}', lang_code = '${lang_code}', author_id = ${author_id} WHERE id = ${id}`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        },
        delete: (db, id) => {
            const query = `DELETE FROM Word WHERE id = ${id}`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        }
    },
    Definition: {
        selectAll: (db) => {
            // Prepare a statement
            const query = `SELECT * FROM Definition`;
            const result = db.exec(query);
            if (result[0]) return {
                query: query,
                result: result[0]
            };
            return {
                query: query,
                result: result
            };
        },
        select: (db, id) => {
            const query = `SELECT * FROM Definition WHERE id = ${id}`;
            const result = db.exec(query);
            if (result[0]) return {
                query: query,
                result: result[0]
            };
            return {
                query: query,
                result: result
            };
        },
        create: (db, synonym_word_id, word, ipa, th, lang_code, author_id) => {
            const query = `INSERT INTO Definition VALUES (NULL, ${synonym_word_id}, '${word}', '${ipa}', '${th}', '${lang_code}', NOW(), ${author_id})`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        },
        update: (db, id, synonym_word_id, word, ipa, th, lang_code, author_id) => {
            const query = `UPDATE Word SET synonym_word_id = ${synonym_word_id}, word = '${word}', ipa = '${ipa}', th = '${th}', lang_code = '${lang_code}', author_id = ${author_id} WHERE id = ${id}`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        },
        delete: (db, id) => {
            const query = `DELETE FROM Definition WHERE id = ${id}`;
            const result = db.exec(query);
            return {
                query: query,
                result: result
            };
        }
    },
}