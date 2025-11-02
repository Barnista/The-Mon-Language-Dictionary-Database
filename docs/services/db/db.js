const DBEngine = {
    init: () => {
        return initSqlJs({
            locateFile: name => './assets/database' + name
        });
    },
    testRun: (SqlJS) => {
        try {
            const db = new SqlJS.Database();
            const result = db.exec("select 'hello world'");
            console.log('Exec script:', result);

            // Run a query without reading the results
            db.run("CREATE TABLE test (col1, col2);");
            // Insert two rows: (1,111) and (2,222)
            db.run("INSERT INTO test VALUES (?,?), (?,?)", [1, 111, 2, 222]);

            // Prepare a statement
            var stmt = db.prepare("SELECT * FROM test WHERE col1 BETWEEN $start AND $end");
            stmt.getAsObject({ $start: 1, $end: 1 }); // {col1:1, col2:111}

            // Bind new values
            stmt.bind({ $start: 1, $end: 2 });
            while (stmt.step()) { //
                var row = stmt.getAsObject();
                // [...] do something with the row of result
                console.log('Test Query:', row);
            }
        } catch (error) {
            throw error
        }
    },
    createDB: (SqlJS, dbTables, dbDatas) => {
        try {
            const db = new SqlJS.Database();
            // Create database according to the design v1
            for (let i = 0; i < dbTables.length; i++) {
                const dbTable = dbTables[i];
                db.run(dbTable);
            }
            for (let i = 0; i < dbDatas.length; i++) {
                const dbData = dbDatas[i];
                db.run(dbData);
            }
            return db;
        } catch (error) {
            throw error;
        }
    },
    insertData: (db, dbData) => {
        try {
            // Create database according to the design v1
            db.run(dbData);
            return db;
        } catch (error) {
            throw error;
        }
    }
}