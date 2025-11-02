import services.dbconfig as dbconfig

from classes.x_category_detail_crud import XCategoryDetailCRUD

import asyncio
import socket
import services.google_translate as google_translate

def check_internet_connection():
    try:
        # Try to connect to a public DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False
    

xcategory_detail_crud = XCategoryDetailCRUD(dbconfig.host, dbconfig.user, dbconfig.password, dbconfig.database2)
xcategory_detail_crud.connect()

details = xcategory_detail_crud.read_by_lang(lang_code='eng')

for dtl in details:
    dtl_id = dtl['id']
    cat_id = dtl['category_id']
    label = dtl['label']
    description = dtl['description']
    tha_translate = asyncio.run(google_translate.translate_eng_to_tha(label))
    xcategory_detail_crud.create(category_id=cat_id, label=tha_translate, description=description, author_id=7, lang_code='tha')
    print(f"CREATED DETAIL: {tha_translate}")
print(f"---- ALL Category Details HAVE BEEN TRANSLATED COMPLETELY ----")
#WARNING: THIS WHOLE PROCESS COULD TAKE 5-10 DAYS !!!