const DB_TABLE = {
    Author: 'Author',
    Category: 'Category',
    CategoryDetail: 'CategoryDetail',
    Word: 'Word',
    Definition: 'Definition',
}

const DB_QUERY_PRESET = {
    SELECT_ALL: `SELECT * FROM {table} LIMIT(5000);`,
    SELECT_WHERE: `SELECT * FROM {table} WHERE {condition} LIMIT(5000);`,
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
    LIMIT(5000);
    `,
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
    LIMIT(5000);
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
        Word as W2 ON W2.synonym_word_id = W1.id
    WHERE 
        W2.synonym_word_id IS NOT NULL AND
        W1.th IS NOT NULL AND
        W2.th IS NOT NULL
    ORDER BY
        W2.word ASC
    LIMIT(5000);
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
    LIMIT(5000);
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
    LIMIT(5000);
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
    LIMIT(5000);
    `,
    SELECT_Definition_Thai_Only: `
    SELECT 
        W1.word as 'Mon Word',
        W1.ipa as 'IPA',
        W1.th as 'TH',
        W2.word as 'Synonym Word',
        D1.definition as 'Definition',
        D1.pos_code as 'Part of Speech',
        A1.name as 'Author'
    FROM 
        Word as W1
    JOIN
        Word as W2 ON W2.synonym_word_id = W1.id
    JOIN 
        Definition as D1 ON W1.id = D1.word_id OR W2.id = D1.word_id
    JOIN 
        Author as A1 ON D1.author_id = A1.id
    WHERE 
        D1.lang_code = 'tha' AND
        W1.word LIKE '%ထေက်%'
    ORDER BY
        W1.word ASC
    LIMIT(5000);
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
    `,
    UNDEFINED_WORDS: `
    SELECT 
         W1.*
    FROM 
         Word as W1
    WHERE 
         W1.synonym_word_id IS NULL AND
         W1.id NOT IN (SELECT W2.id FROM  Word as W2 JOIN Definition as D2 ON D2.word_id = W2.id WHERE D2.lang_code IN ('tha', 'mya', 'eng'));
    `,
    CONFUSING_DIACRITICS_1: `
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
        Word.word LIKE '%ံ%' AND 
        Definition.author_id IN (1, 2, 3) AND
        Word.ipa = '???'
    ORDER BY
        Word.word;
    `,
    WORDS_WITH_ORIGINAL_TH: ` 
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
        Word.th LIKE '%(og)%' AND
        Word.author_id IN (2, 3)
    ORDER BY
        Word.word;
    `,
}