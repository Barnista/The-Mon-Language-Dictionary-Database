import mysql.connector
from mysql.connector import Error

class XCategoryDetailCRUD:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4'
            )
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.conn = None

    def close(self):
        if self.conn:
            self.conn.close()

    def create(self, category_id, label, description, author_id, lang_code='eng'):
        sql = '''INSERT INTO CategoryDetail (category_id, label, description, author_id, created_at, lang_code)
                 VALUES (%s, %s, %s, %s, NOW(), %s)'''
        vals = (category_id, label, description, author_id, lang_code)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, vals)
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating category_detail: {e}")
            return None
        #finally:
        #    cursor.close()

    def read_all(self):
        sql = '''SELECT * FROM CategoryDetail'''
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def read_one(self, category_id):
        sql = '''SELECT * FROM CategoryDetail WHERE category_id = %s'''
        vals = (category_id)
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, vals)
            return cursor.fetchone()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def update_one(self, category_id, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = %s")
            values.append(value)
        if not fields:
            print("No fields to update.")
            return False
        sql = f"UPDATE CategoryDetail SET {', '.join(fields)} WHERE category_id = %s"
        values.append(category_id)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, tuple(values))
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error updating word: {e}")
            return False
        #finally:
        #    cursor.close()

    def delete_one(self, category_id):
        sql = '''DELETE FROM CategoryDetail WHERE category_id = %s'''
        vals = (category_id)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, vals)
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting word: {e}")
            return False
        #finally:
        #    cursor.close()

    def delete_all(self):
        sql = '''DELETE FROM CategoryDetail'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error deleting words: {e}")
            return 0
        #finally:
        #    cursor.close()
