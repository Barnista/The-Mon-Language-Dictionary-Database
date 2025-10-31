import services.dbconfig as dbconfig

from alphabets.lib_alphabet import LibAlphabet
from classes.x_word_crud import XWordCRUD

xword_crud = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xword_crud.connect()

# try the current model of Mon Alphabet AI
alphabet_ai = LibAlphabet()

def analyse_text(word):
    try:
        result = alphabet_ai.analyse_text(word)
        print("------------------ IPA and TH generation results -----------------")
        print(f"Analysis Results: {result['text']}")
        print(f"Result count: {len(result)}")
        for i, res in enumerate(result['ipas']):
            print(f"  ipa: {res}")
        for i, res in enumerate(result['ths']):
            print(f"  th: {res}")
    except Exception as e:
        print(f"Error Word: {word}")
        print(f"Error: {str(e)}")
    pass

#Test cases
analyse_text('အက္ခရ်မန်')
analyse_text('မင်္ဂလာပါ')
analyse_text('အေပ်ပလဳဂေရှေန်')
analyse_text('ဂယးသဝ်တ္ၚဲ')
analyse_text('တ္ၚဲ')