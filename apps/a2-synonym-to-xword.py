import services.dbconfig as dbconfig

from classes.synonym_crud import SynonymCRUD
from classes.x_word_crud import XWordCRUD

# Operations can be performed using conn1 and conn2
synonym_crud = SynonymCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database1)
synonym_crud.connect()
synonyms = synonym_crud.read_all()

#author_id = 1 => NaiSacLun
#author_id = 2 => AnontaMon

xword_crud = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xword_crud.connect()

for word in synonyms:
    xword = xword_crud.create(
        word=word['synonym'],
        ipa=None,
        th=None,
        lang_code='mnw',
        author_id=1,
        synonym_word_id=word['word_id']
    )


# Don't forget to close connections when done
synonym_crud.close()
xword_crud.close()