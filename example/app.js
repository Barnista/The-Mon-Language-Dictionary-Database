start();

async function start() {
    try {
        const engine = await DBEngine.init();
        DBEngine.testRun(engine);

        const db = DBEngine.createDB(
            engine, 
            DB_TABLES,
            [
                DB_DATA_AUTHORS,
                DB_DATA_CATEGORIES,
                DB_DATA_CATEGORY_DETAILS,
                DB_DATA_WORDS_1,
                DB_DATA_WORDS_2,
                DB_DATA_WORDS_3
            ]
        );

        const authors = DB_QUERY.Author.selectAll(db);
        console.log(authors);
    } catch (error) {
        console.log(error);
    }
}
