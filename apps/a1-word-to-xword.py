import services.dbconfig as dbconfig

from classes.word_crud import WordCRUD
from classes.x_word_crud import XWordCRUD


# Connection details
host = 'localhost'
user = 'root'
password = 'barnista27'


# Operations can be performed using conn1 and conn2
word_crud = WordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database1)
word_crud.connect()
words = word_crud.read_all()
print(words)

#author_id = 1 => NaiSacLun
#author_id = 2 => AnontaMon

xword_crud = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xword_crud.connect()

for word in words:
    xword = xword_crud.create_with_id(
        id=word['word_id'],
        word=word['word'],
        ipa=word['pronunciation'],
        th=None,
        lang_code='mnw',
        author_id=1,
        synonym_word_id=None
    )


# Don't forget to close connections when done
word_crud.close()
xword_crud.close()