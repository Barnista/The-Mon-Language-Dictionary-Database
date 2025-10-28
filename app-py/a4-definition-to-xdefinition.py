import services.dbconfig as dbconfig

from classes.definition_crud import DefinitionCRUD
from classes.x_definition_crud import XDefinitionCRUD

# Operations can be performed using conn1 and conn2
definition_crud = DefinitionCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database1)
definition_crud.connect()
definitions = definition_crud.read_all()
print(definitions)

xdefinition_crud = XDefinitionCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xdefinition_crud.connect()

for defn in definitions:
    definition_id = defn['definition_id']
    print(f"Processing definition_id: {definition_id}")
    word_id = defn['word_id']
    language_id = defn['language_id']
    pos_id = defn['pos_id']
    definition = defn['definition']
    example = defn['example']
    category_id = defn['category_id']

    # Map language_id to lang_code
    lang_code_map = {1: 'eng', 2: 'mnw', 3: 'mya', 4: 'tha'}
    lang_code = lang_code_map.get(language_id, 'unknown')

    # Map pos_id to pos_code
    pos_code_map = {1: 'n', 2: 'pron', 3: 'adj', 4: 'v', 5: 'adv', 6: 'prep', 7: 'conj', 8: 'interj', 9: 'uncl', 10: 'pali', 11: 'pali_sansakrit', 12: 'sansakrit', 13: 'myan', 14: 'eng', 15: 'tha', 16: 'Hynd', 17: 'Unknown', 18: 'malay', 19: 'ben', 20: 'num'}
    pos_code = pos_code_map.get(pos_id, 'other')

    xdefinition = xdefinition_crud.create(
        word_id=word_id,
        lang_code=lang_code,
        pos_code=pos_code,
        definition=definition,
        example=example,
        category_id=category_id,
        author_id=1
    )
    print(f"Created xdefinition with ID: {xdefinition}")

# Don't forget to close connections when done
definition_crud.close()
xdefinition_crud.close()