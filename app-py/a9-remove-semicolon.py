import services.dbconfig as dbconfig

import time
from classes.x_definition_crud import XDefinitionCRUD

xdefinition_crud = XDefinitionCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xdefinition_crud.connect()

definitions = xdefinition_crud.read_by_definition_like('%;%')
for dfn in definitions:
    word_id = dfn['word_id']
    dfn_id = dfn['id']
    definition = dfn['definition']
    definition = definition.replace(";", ",")
    definition = definition.replace('\\', "/")
    xdefinition_crud.update_one(dfn_id, definition=definition)

print("REMOVED ALL SEMICOLONS ON DEFINITION TO AVOID ALGORITHM BUGS")

