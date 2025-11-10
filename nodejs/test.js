/*
    This is a test running to show that the library works efficiently as intended
*/
import { MonDictDB } from "./index.js"; 

MonDictDB.startDB().then(payload => {
    console.log('PAYLOAD READY', payload);
    MonDictDB.searchByWord(payload, 'က', false, 999, true, 'eng', [1, 2, 3], 'ASC').then(vals => {
        console.log('EX. SEARCH', vals.length, '(count)');
    });
})