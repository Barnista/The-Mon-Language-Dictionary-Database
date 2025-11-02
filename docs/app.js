const radio_table_1 = document.getElementById('table1');
const radio_table_2 = document.getElementById('table2');
const radio_table_3 = document.getElementById('table3');
const radio_table_4 = document.getElementById('table4');
const radio_table_5 = document.getElementById('table5');

const radio_query_1 = document.getElementById('query1');
const radio_query_2 = document.getElementById('query2');
const radio_query_3 = document.getElementById('query3');
const radio_query_4 = document.getElementById('query4');
const radio_query_5 = document.getElementById('query5');
const radio_query_6 = document.getElementById('query6');
const radio_query_7 = document.getElementById('query7');
const radio_query_8 = document.getElementById('query8');
const radio_query_9 = document.getElementById('query9');
const radio_query_10 = document.getElementById('query10');
const radio_query_11 = document.getElementById('query11');
const radio_query_12 = document.getElementById('query12');
const radio_query_13 = document.getElementById('query13');
const radio_query_14 = document.getElementById('query14');
const radio_query_15 = document.getElementById('query15');
const radio_query_16 = document.getElementById('query16');
const radio_query_17 = document.getElementById('query17');


let h_output = document.getElementById('h-output');
let data_div = document.getElementById('data-div');
let data_table = null;
const error_label = document.getElementById('error-label');
const btn_run = document.getElementById('btn-run');

let selected_table = DB_TABLE.Word;
let selected_query = DB_QUERY_PRESET.SELECT_ALL;
let built_query = "";
let result = null;
let is_loading = false;

start();

async function start() {
    try {
        const engine = await DBEngine.init();
        DBEngine.testRun(engine);

        const db = DBEngine.createDB(
            engine,
            [
                DB_TABLES_1,
                DB_TABLES_2,
                DB_TABLES_3,
                DB_TABLES_4,
                DB_TABLES_5
            ],
            [
                DB_DATA_AUTHOR_1,
                DB_DATA_CATEGORY_1,
                DB_DATA_CATEGORYDETAIL_1,
                DB_DATA_WORD_1,
                DB_DATA_WORD_2,
                DB_DATA_WORD_3,
            ]
        );

        DBEngine.insertData(db, DB_DATA_DEFINITION_1);
        DBEngine.insertData(db, DB_DATA_DEFINITION_2);
        DBEngine.insertData(db, DB_DATA_DEFINITION_3);
        DBEngine.insertData(db, DB_DATA_DEFINITION_4);
        DBEngine.insertData(db, DB_DATA_DEFINITION_5);
        DBEngine.insertData(db, DB_DATA_DEFINITION_6);
        DBEngine.insertData(db, DB_DATA_DEFINITION_7);
        DBEngine.insertData(db, DB_DATA_DEFINITION_8);
        DBEngine.insertData(db, DB_DATA_DEFINITION_9);
        DBEngine.insertData(db, DB_DATA_DEFINITION_10);
        DBEngine.insertData(db, DB_DATA_DEFINITION_11);
        DBEngine.insertData(db, DB_DATA_DEFINITION_12);
        DBEngine.insertData(db, DB_DATA_DEFINITION_13);
        DBEngine.insertData(db, DB_DATA_DEFINITION_14);
        DBEngine.insertData(db, DB_DATA_DEFINITION_15);
        DBEngine.insertData(db, DB_DATA_DEFINITION_16);
        DBEngine.insertData(db, DB_DATA_DEFINITION_17);
        DBEngine.insertData(db, DB_DATA_DEFINITION_18);
        DBEngine.insertData(db, DB_DATA_DEFINITION_19);
        DBEngine.insertData(db, DB_DATA_DEFINITION_20);
        DBEngine.insertData(db, DB_DATA_DEFINITION_21);
        DBEngine.insertData(db, DB_DATA_DEFINITION_22);
        DBEngine.insertData(db, DB_DATA_DEFINITION_23);
        DBEngine.insertData(db, DB_DATA_DEFINITION_24);

        initGUI(engine, db);
        rebuildQuery();
        execQuery(db, built_query, false);
    } catch (error) {
        console.log(error);
    }
}

function initGUI(engine, db) {
    radio_table_1.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectTable(DB_TABLE.Word);
        }
    });
    radio_table_2.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectTable(DB_TABLE.Definition);
        }
    });
    radio_table_3.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectTable(DB_TABLE.Category);
        }
    });
    radio_table_4.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectTable(DB_TABLE.CategoryDetail);
        }
    });
    radio_table_5.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectTable(DB_TABLE.Author);
        }
    });

    radio_query_1.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_PRESET.SELECT_ALL);
        }
    });

    radio_query_2.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_PRESET.SELECT_WHERE);
        }
    });

    radio_query_3.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_PRESET.SELECT_COUNT);
        }
    });

    radio_query_4.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_PRESET.SELECT_DISTINCT);
        }
    });

    radio_query_5.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_PRESET.INSERT_INTO);
        }
    });

    radio_query_6.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_PRESET.UPDATE);
        }
    });


    radio_query_7.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_PRESET.DELETE);
        }
    });

    radio_query_8.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.SELECT_Word_JOIN_Definition_JOIN_Author);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_9.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.SELECT_Word_JOIN_Definition_WHERE_Definition);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_10.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.SELECT_Word_JOIN_Word_WHERE_Synonym);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_11.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.SELECT_Word_JOIN_Definition_WHERE_IS_Pronoun);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_12.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.SELECT_Definition_JOIN_Category_WHERE);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_13.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.SELECT_Definition_JOIN_Word_WHERE_Definition);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_14.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.SELECT_Definition_Thai_Only);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_15.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.SELECT_Author_Summary);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_16.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.UNDEFINED_WORDS);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    radio_query_17.addEventListener('click', function (event) {
        if (event.target && event.target.matches("input[type='radio']")) {
            // switch to selected table
            selectQuery(DB_QUERY_INSTANTS.CONFUSING_DIACRITICS_1);
            //AUTO SCROLL DOWN
            scrollToSQLHilight();
        }
    });

    btn_run.addEventListener('click', function (event) {
        if (built_query) {
            console.log(built_query);
            execQuery(db, built_query, true);
        }
    });
}

function selectTable(table) {
    selected_table = table;
    rebuildQuery()
}

function selectQuery(query) {
    selected_query = query;
    rebuildQuery()
}

function rebuildQuery() {
    built_query = selected_query;
    built_query = built_query.replace("{table}", selected_table);
    console.log(`built query: ${built_query}`);
    hilighCode();
}

function hilighCode() {
    const code = document.getElementById('sql-hilight');
    if (code && code.dataset.highlighted) {
        delete code.dataset.highlighted;
    }
    code.textContent = built_query;
    hljs.highlightBlock(code); // Re-highlight
}

function scrollToSQLHilight() {
    const hcode = document.getElementById('h-sql');
    hcode.scrollIntoView({ behavior: 'smooth' });
}

async function execQuery(db, query, isScrollResult) {
    try {
        const r = await db.exec(query);
        if (r[0]) {
            result = r[0];
            await displayResult(selected_table, result.columns, result.values, isScrollResult);
            toggleErrorLabel(false, null);
        } else {
            displayNoResult(selected_table);
        }
    } catch (error) {
        toggleErrorLabel(true, error);
        toggleDataDiv(true, error);
    }
}

function toggleErrorLabel(bool, msg) {
    if (bool) {
        $('#error-label').show();
        if (msg) error_label.innerHTML = msg.toString();
        else error_label.innerHTML = 'Error: UNKNOWN...';
        error_label.scrollIntoView({ behavior: 'smooth' });
    } else {
        $('#error-label').hide();
    }
}

function displayResult(table_name, columns, values, isScrollResult) {
    toggleDataDiv(false, null);

    let col_arr = [];
    for (let i = 0; i < columns.length; i++) {
        const element = columns[i];
        col_arr.push({ data: element, title: element });
    }
    console.log(col_arr);

    let val_arr = [];
    for (let i = 0; i < values.length; i++) {
        const vals = values[i];
        let obj = {};
        for (let k = 0; k < vals.length; k++) {
            const item = vals[k];
            obj[columns[k]] = item;
        }
        val_arr.push(obj);
    }
    console.log(val_arr);

    if (data_table) {
        data_table.destroy();
        $('#data-table').empty();
    }
    data_table = $('#data-table').DataTable({
        data: val_arr,
        columns: col_arr,
        pageLength: 25
    });

    // Scrolls the target element into view, optionally with smooth animation.
    if (isScrollResult) h_output.scrollIntoView({ behavior: 'smooth' });
}

function displayNoResult() {
    console.log('No result found.');
    //if (data_table) {
    //    data_table.destroy();
    //    $('#data-table').empty();
    //}

    toggleDataDiv(true, null);
}

function toggleDataDiv(bool, msg) {
    if (bool) {
        $('#data-div').show();
        $('#data-table').hide();
        if (msg) data_div.innerHTML = `<span class="text-danger">${msg.toString()}</span>`;
        else data_div.innerHTML = 'No result found.';
        // Scrolls the target element into view, optionally with smooth animation.
        h_output.scrollIntoView({ behavior: 'smooth' });
    } else {
        $('#data-div').hide();
        $('#data-table').show();
    }
}

function activateEditor(event) {
    const container = document.getElementById("sql-container");

    // Prevent re-activating if already in textarea mode
    if (container.querySelector("textarea")) return;

    const textarea = document.createElement("textarea");
    textarea.id = "sql-input";
    textarea.className = "form-control p-3";
    textarea.value = built_query;
    textarea.rows = 6;

    // Replace code block with textarea
    container.innerHTML = "";
    container.appendChild(textarea);
    textarea.focus();

    // When textarea loses focus, revert to code block
    textarea.addEventListener("blur", () => {
        const newCode = document.createElement("code");
        newCode.id = "sql-hilight";
        newCode.className = "language-sql vscode-sql p-3 shadow";
        newCode.textContent = textarea.value;
        built_query = textarea.value;

        const pre = document.createElement("pre");
        pre.appendChild(newCode);

        container.innerHTML = "";
        container.appendChild(pre);
        hljs.highlightBlock(newCode); // Re-highlight
    });
}

