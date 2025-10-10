from classes.category_crud import CategoryCRUD
from classes.x_category_detail_crud import XCategoryDetailCRUD
from classes.x_category_crud import XCategoryCRUD

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
category_crud = CategoryCRUD(host, user, password, 'mondictionary_v2')
category_crud.connect()
categories = category_crud.read_all()
print(categories)

xcategory_crud = XCategoryCRUD(host, user, password, 'TheMonLanguageDictionary')
xcategory_crud.connect()

xcategory_detail = XCategoryDetailCRUD(host, user, password, 'TheMonLanguageDictionary')
xcategory_detail.connect()

for cat in categories:
    category_id = cat['category_id']
    print(f"Processing category_id: {category_id}")
    parent_category_id = cat['parent_category_id']
    en_category_name = cat['en_category_name']
    mm_category_name = cat['mm_category_name']
    mon_category_name = cat['mon_category_name']
    description = cat['description']

    #category = xcategory_crud.create_with_id(
    #    category_id=category_id,
    #    parent_category_id=parent_category_id,
    #    name=en_category_name,
    #    author_id=1
    #)
    category_detail = xcategory_detail.create(
        category_id=category_id,
        label=en_category_name,
        description=description,
        author_id=1,
        lang_code='eng'
    )
    category_detail2 = xcategory_detail.create(
        category_id=category_id,
        label=mm_category_name,
        description=description,
        author_id=1,
        lang_code='mya'
    )
    category_detail3 = xcategory_detail.create(
        category_id=category_id,
        label=mon_category_name,
        description=description,
        author_id=1,
        lang_code='mnw'
    )


# Don't forget to close connections when done
conn1.close()
conn2.close()