import services.dbconfig as dbconfig

from classes.x_word_crud import XWordCRUD
from classes.x_definition_crud import XDefinitionCRUD

import asyncio
import time
import socket
import services.google_translate as google_translate

def check_internet_connection():
    try:
        # Try to connect to a public DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False
    

xword_crud = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xword_crud.connect()

xdefinition_crud = XDefinitionCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xdefinition_crud.connect()

#PHASE 1 - EST. 10-14 hours -- 16% done
#words = xword_crud.read_with_limit(1, 5000)
#PHASE 2 - EST. 10-14 hours -- 32% done
words = xword_crud.read_with_limit(5001, 10000)
##PHASE 3 - EST. 10-14 hours -- 48% done
#words = xword_crud.read_with_limit(10001, 15000)
#PHASE 4 - EST. 10-14 hours -- 64% done
#words = xword_crud.read_with_limit(15001, 20000)
##PHASE 5 - EST. 10-14 hours -- 70% done
#words = xword_crud.read_with_limit(20001, 25000)
##PHASE 6 - EST. 10-14 hours -- 86% done
#words = xword_crud.read_with_limit(25001, 30000)
##PHASE 7 - EST. 1 hours -- 100% done
#words = xword_crud.read_with_limit(30001, 35000)


for word in words:
    word_id = word['id']
    definitions = xdefinition_crud.read_by_word_id(word_id)
    print(f"Word ID: {word_id} | Definitions: {definitions}")
    if len(definitions) > 0:
        # Word already has some definitions, translation the missing ones (English, Thai, or Myanmese)
        translates = list()
        for defn in definitions:
            lang_code = defn['lang_code']
            pos_code = defn['pos_code']
            definition = defn['definition']
            example = defn['example']
            category_id = defn['category_id']

            #CHECK INTERNET CONNECTION BEFORE USING GOOGLE TRANSLATE API
            while not check_internet_connection():
                print("No internet connection. Retrying...")
                time.sleep(5)  # Wait for 5 seconds before retrying

            if pos_code != 'other':
                # Exclude synonym words in the process of translation, we'll do it later in a8.py script
                if lang_code == 'tha':
                    eng_translate = asyncio.run(google_translate.translate_tha_to_eng(definition))
                    mya_translate = asyncio.run(google_translate.translate_tha_to_mya(definition))
                    translates.append(('tha', pos_code, definition, example, category_id))
                    translates.append(('eng', pos_code, eng_translate, example, category_id))
                    translates.append(('mya', pos_code, mya_translate, example, category_id))
                elif lang_code == 'mya':
                    eng_translate = asyncio.run(google_translate.translate_mya_to_eng(definition))
                    tha_translate = asyncio.run(google_translate.translate_mya_to_tha(definition))
                    translates.append(('mya', pos_code, definition, example, category_id))
                    translates.append(('eng', pos_code, eng_translate, example, category_id))
                    translates.append(('tha', pos_code, tha_translate, example, category_id))
        # filter only unique translations within variable 'translates'
        unique_translates = list(set(translates))
        for lang_code, pos_code, definition, example, category_id in unique_translates:
            existing_dfn = xdefinition_crud.read_by_lang_pos_and_definition(lang_code=lang_code, pos_code=pos_code, definition=definition)
            if len(existing_dfn) == 0:
                # the word does not exist yet
                # create new definition with author_id=7 (Google Translate API)
                xdefinition_crud.create(
                    word_id=word_id,
                    lang_code=lang_code,
                    pos_code=pos_code,
                    definition=definition,
                    example=example,
                    category_id=category_id,
                    author_id=7
                )
                print(f"Created definition: {definition} for word_id {word_id}")
    #sleep for 5 sec before continuing to the next word
    print('PREPARE TO TRANSLATE THE NEXT WORD IN 10 SEC (TRY NOT TO SPAM REUEST TOO MUCH)')
    time.sleep(10)
print(f"---- ALL WORDS HAVE BEEN TRANSLATED COMPLETELY ----")
#WARNING: THIS WHOLE PROCESS COULD TAKE 5-10 DAYS !!!