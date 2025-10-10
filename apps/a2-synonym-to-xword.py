from classes.synonym_crud import SynonymCRUD
from classes.x_word_crud import XWordCRUD

import mysql.connector

# Connection details
host = 'localhost'
user = 'root'
password = 'barnista27'

# Connect to mondictionary_v2
conn1 = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database='mondictionary_v2'
)
print("Connected to mondictionary_v2")

# Connect to TheMonLanguageDictionary
conn2 = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database='TheMonLanguageDictionary'
)
print("Connected to TheMonLanguageDictionary")


# Operations can be performed using conn1 and conn2
synonym_crud = SynonymCRUD(host, user, password, 'mondictionary_v2')
synonym_crud.connect()
synonyms = synonym_crud.read_all()

#author_id = 1 => NaiSacLun
#author_id = 2 => AnontaMon

xword_crud = XWordCRUD(host, user, password, 'TheMonLanguageDictionary')
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
conn1.close()
conn2.close()