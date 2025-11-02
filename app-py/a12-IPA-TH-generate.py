from alphabets.lib_alphabet import LibAlphabet

# try the current model of Mon Alphabet AI
alphabet_ai = LibAlphabet()

def analyse_text(word, debug=False):
    try:
        result = alphabet_ai.analyse_text(word, debug=debug)
        print("------------------ IPA and TH generation results -----------------")
        print(f"Analysis Results: {result['text']}")
        print(f"Result count: {len(result)}")
        for i, res in enumerate(result['ipas']):
            print(f"  ipa: {res}")
        for i, res in enumerate(result['ths']):
            print(f"  th: {res}")
        return result
    except Exception as e:
        print(f"Error Word: {word}")
        print(f"Error: {str(e)}")
        return None
    pass

#Test cases
# analyse_text('အက္ခရ်မန်', debug=False)
# analyse_text('မင်္ဂလာပါ', debug=False)
# analyse_text('အေပ်ပလဳဂေရှေန်', debug=False)
# analyse_text('ဂယးသဝ်တ္ၚဲ', debug=False)
# analyse_text('တ္ၚဲ', debug=False)
# analyse_text('နွံ', debug=False)
# analyse_text('မွဲ', debug=False)
# analyse_text('ကွေံ', debug=False)
# analyse_text('ဇွဟ်', debug=False)
# analyse_text('မ္ၚဵုရအဴ', debug=False)
# analyse_text('သ္ၚ', debug=True)
# analyse_text('သ္ဇ', debug=True)

import services.dbconfig as dbconfig
import time
from classes.x_word_crud import XWordCRUD

xword_crud = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xword_crud.connect()

words = xword_crud.read_all()

for word_entry in words:
    word = word_entry.get('word', '')
    id = word_entry.get('id', None)
    analysed = analyse_text(word, debug=False)

    ipa = analysed['ipa'] if analysed else ''
    th = analysed['th'] if analysed else ''

    #check if th already exists, if so, skip updating th
    exth = word_entry.get('th', None)
    if exth != None and exth != '' and exth != '???':
        th = exth + " (og)"
    xword_crud.update_one(id, ipa=ipa, th=th)
    print(f"===================> Next Word (ID: {id}) ===================>")
    #time.sleep(0.1)  # to avoid overwhelming the system