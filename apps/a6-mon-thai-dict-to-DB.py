import services.dbconfig as dbconfig

import pandas as pd
from classes.x_word_crud import XWordCRUD
from classes.x_definition_crud import XDefinitionCRUD

import services.part_of_speech as part_of_speech

xword_crud = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xword_crud.connect()

xdefinition_crud = XDefinitionCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xdefinition_crud.connect()

# Load CSV file into DataFrame
df = pd.read_csv("./csv/mon-thai-dict-processed.csv")

# Display the DataFrame as a table
#print(df)

word_sets = list(zip(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3]))

#print(word_sets)

# Process each pair to SQL INSERTION statements
for mon, pronunciation, pos, th in word_sets:
    #Remove number and the following dot if present
    #eng = asyncio.run(google_translate.translate_tha_to_eng(th))
    #mya = asyncio.run(google_translate.translate_tha_to_mya(th))
    #print(f"Mon: {mon} | Pronunciation: {pronunciation} | POS: {pos} | Thai: {th} | Myanmar: {mya} | English: {eng}")
    
    eng_pos = part_of_speech.get_pos_code_from_thai_tag(pos)

    # search for existing word
    words = xword_crud.read_by_word(mon)
    if len(words) > 0:
        print(f"Word '{mon}' already exists. Skipping insertion.")
        existing_word = words[0]
        word_id = existing_word['id']
        if word_id:
            xword_crud.update_one(
                word_id=word_id, 
                th=pronunciation, 
                author_id=3 # Both dictionary compilers included the same word
            )
            xdefinition_crud.create(
                word_id=word_id,
                lang_code='tha',
                pos_code=eng_pos,
                definition=th,
                example=None,
                category_id=None,
                author_id=2
            )
            print(f"Added definition for existing word ID {word_id}.")
    else:
        last_id = xword_crud.create(
            word=mon,
            ipa='',
            th=pronunciation,
            lang_code='mnw',
            author_id=2,
            synonym_word_id=None
        )
        if last_id:
            xdefinition_crud.create(
                word_id=last_id,
                lang_code='tha',
                pos_code=eng_pos,
                definition=th,
                example=None,
                category_id=None,
                author_id=2
            )
        print(f"Inserted word '{mon}' with ID {last_id} and its definition.")

    #print(f"INSERT INTO X_Word (word, ipa, th, mya, eng, lang_code, author_id) VALUES ('{mon}', '{pronunciation}', '{th}', '{mya}', '{eng}', 'mnw', 2);")


