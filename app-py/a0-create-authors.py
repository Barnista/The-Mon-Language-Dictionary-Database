import services.dbconfig as dbconfig

from classes.x_author_crud import XAuthorCRUD

xauthor_crud = XAuthorCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xauthor_crud.connect()

#create authors Nai Sac Lun (id=1) and Anonta Mon (id=2)
author1_id = xauthor_crud.create_with_id(
    id=1,
    name='Nai Sac Lun',
    bio='Mon-Burmese Dictionar Compiler.',
)

author2_id = xauthor_crud.create_with_id(
    id=2,
    name='Anonta Mon',
    bio='Mon-Thai Dictionary Compiler.',
)

author3_id = xauthor_crud.create_with_id(
    id=3,
    name='Nai Sac Lun & Anonta Mon',
    bio='Nai Sac Lun and Anonta Mon combination.',
)

author4_id = xauthor_crud.create_with_id(
    id=4,
    name='Barnista',
    bio='Project Lead, The Mon Language Dictionary Database.',
)

author5_id = xauthor_crud.create_with_id(
    id=5,
    name='Nai Saik Chan',
    bio='Co-developer, The Mon Language Dictionary Database.',
)

author6_id = xauthor_crud.create_with_id(
    id=6,
    name='Htaw Mon',
    bio='Co-developer, The Mon Language Dictionary Database.',
)

author7_id = xauthor_crud.create_with_id(
    id=7,
    name='Google Translate API',
    bio='Automated translations provided by Google Translate API.',
)

author8_id = xauthor_crud.create_with_id(
    id=8,
    name='Community Contributions',
    bio='Definitions and examples contributed by the community.',
)
