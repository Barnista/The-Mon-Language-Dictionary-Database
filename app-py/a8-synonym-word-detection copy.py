import services.dbconfig as dbconfig

import time
from classes.x_word_crud import XWordCRUD
from classes.x_definition_crud import XDefinitionCRUD

xword_crud = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xword_crud.connect()

xdefinition_crud = XDefinitionCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xdefinition_crud.connect()

definitions = xdefinition_crud.read_by_pos_code('other')
count = 0
for dfn in definitions:
    word_id = dfn['word_id']
    dfn_id = dfn['id']
    definition = dfn['definition']
    definition = definition.replace(" ", "")
    synonym = definition.replace("ดู", "")

    parent_words = xword_crud.read_by_word(synonym)
    child_word = xword_crud.read_one(word_id)
    if len(parent_words) > 0:
        # Parent words detected
        count = count + 1
        parent_word = parent_words[0]
        print(f"Parent Word Detected: {parent_word['word']} | ID: {parent_word['id']} | Synonym: {child_word['word']} | SynonymID: {child_word['id']}")
        # time.sleep(1)
        #delay 1 second each item
        parent_id = parent_word['id']
        child_id = child_word['id']
        xword_crud.update_one(child_id, synonym_word_id=parent_id)
        #DELETE UNUSED DEFINITION 
        xdefinition_crud.delete_one(dfn_id)
print(f"REFERENCED SYNONYM TO PARENT WORDS COUNT: {count}")

