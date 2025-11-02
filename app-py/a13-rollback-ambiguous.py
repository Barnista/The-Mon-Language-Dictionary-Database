# Try to remove ipa and th from words that have ambiguous diacritic "ံ". The, rollback those words to empty ipa and some valued th.

import services.dbconfig as dbconfig
from classes.x_word_crud import XWordCRUD
import time

xword_backup = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, 'BackupA11_TheMonLanguageDictionary')
xword_backup.connect()

xword_crud = XWordCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xword_crud.connect()

ambiguous1 = "ံ"

xword_crud.update_filter_in_diacritic(ambiguous1, ipa='???', th='???')

words = xword_crud.read_filter_in_diacritic(ambiguous1)

for word_entry in words:
    id = word_entry.get('id', None)
    synonym_word_id = word_entry.get('synonym_word_id', None)
    backup_entry = xword_backup.read_one(id)
    if backup_entry:
        th_backup = backup_entry['th']
        ipa_backup = backup_entry['ipa']
        if th_backup == None: 
            th_backup = '???'
        else:
            th_backup = th_backup + ' (og)'
        if ipa_backup == None: 
            ipa_backup = '???'
        else:
            ipa_backup = ipa_backup + ' (og)'

        # if there is a synonym, get its synonym ipa and th value:
        synonym = xword_crud.read_one(synonym_word_id)
        if synonym:
            synonym_ipa = synonym.get('ipa', '')
            synonym_th = synonym.get('th', '')
            if synonym_ipa and synonym_ipa != '???':
                ipa_backup = synonym_ipa+' (sn)'
            if synonym_th and synonym_th != '???':
                th_backup = synonym_th+' (sn)'
        
        xword_crud.update_one(id, th=th_backup, ipa=ipa_backup)
        print(f"ROLLED BACK Word ID: {id} with IPA: {ipa_backup} || TH: {th_backup}")
        #time.sleep(0.01)  # to avoid overwhelming the system