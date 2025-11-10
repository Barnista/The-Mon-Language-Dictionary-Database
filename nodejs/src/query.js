export const DB_TABLE = {
    Author: 'Author',
    Category: 'Category',
    CategoryDetail: 'CategoryDetail',
    Word: 'Word',
    Definition: 'Definition',
}

export const DB_QUERY_PRESET = {
    SELECT_ALL(table) {
        return `SELECT * FROM {table} LIMIT(5000);`
            .replace('{table}', table)
    },
    SELECT_WHERE(table, condition, limit) {
        return `SELECT * FROM {table} WHERE {condition} LIMIT({limit});`
            .replace('{table}', table)
            .replace('{condition}', condition)
            .replace('{limit}', limit)
    },
    SELECT_COUNT(table) {
        return `SELECT COUNT(*) FROM {table};`
            .replace('{table}', table)
    },
    SELECT_DISTINCT(table, column) {
        return `SELECT DISTINCT {column} FROM {table};`
            .replace('{table}', table)
            .replace('{column}', column)
    },
    INSERT_INTO(table, columns, values) {
        return `INSERT INTO {table} ({columns}) VALUES ({values});`
            .replace('{table}', table)
            .replace('{columns}', columns)
            .replace('{values}', values)

    },
    UPDATE(table) {
        return `UPDATE {table} SET {column1} = {value1}, {column2} = {value2} WHERE {condition};`
            .replace('{table}', table)
    },
    DELETE(table, condition) {
        return `DELETE FROM {table} WHERE {condition};`
            .replace('{table}', table)
            .replace('{condition}', condition)
    }
}

export const DB_QUERY_INSTANTS = {
    SELECT_WORD_WITH_LIMIT(word, isLimit, limit, isFirstCharOnly, lang_code, includeAuthorIds, orderBy) {
        return `
        SELECT 
            Word.id as 'id',
            Word.word as 'word',
            Word.ipa as 'ipa',
            Word.th as 'th',
            A1.name as 'authorName',
            A1.id as 'authorId',
            Definition.definition as 'definition',
            Definition.pos_code as 'pos_code',
            A2.name as 'authorDefName',
            A2.id as 'authorDefId'
        FROM 
            Word
        JOIN 
            Definition ON Word.id = Definition.word_id
        JOIN 
            Author as A1 ON Word.author_id = A1.id
        JOIN 
            Author as A2 ON Definition.author_id = A2.id
        WHERE 
            Word.word LIKE '${isFirstCharOnly ? '' : '%'}${word}%'
            ${lang_code ? `AND Definition.lang_code = '${lang_code}'` : ''}
            ${includeAuthorIds && includeAuthorIds.length > 0 ? `AND Word.author_id IN (${includeAuthorIds.join(',')})` : ''}
        ORDER BY
            Word.id ${orderBy}
        ${isLimit ? `LIMIT(${limit})` : ''}
        `
    },
    SELECT_WORD_FROM_DEFINITION(word, isLimit, limit, isFirstCharOnly, lang_code, includeAuthorIds, orderBy) {
        
        return `
        SELECT 
            Word.id as 'id',
            Word.word as 'word',
            Word.ipa as 'ipa',
            Word.th as 'th',
            A1.name as 'authorName',
            A1.id as 'authorId',
            Definition.definition as 'definition',
            Definition.pos_code as 'pos_code',
            A2.name as 'authorDefName',
            A2.id as 'authorDefId'
        FROM 
            Word
        JOIN 
            Definition ON Word.id = Definition.word_id
        JOIN 
            Author as A1 ON Word.author_id = A1.id
        JOIN 
            Author as A2 ON Definition.author_id = A2.id
        WHERE 
            Definition.definition LIKE '${isFirstCharOnly ? '' : '%'}${word}%'
            ${lang_code ? `AND Definition.lang_code = '${lang_code}'` : ''}
            ${includeAuthorIds && includeAuthorIds.length > 0 ? `AND Word.author_id IN (${includeAuthorIds.join(',')})` : ''}
        ORDER BY
            Definition.definition ${orderBy}
        ${isLimit ? `LIMIT(${limit})` : ''}
        `
    }
}