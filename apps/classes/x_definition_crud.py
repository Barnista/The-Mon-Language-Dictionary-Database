import mysql.connector
from mysql.connector import Error

class XDefinitionCRUD:
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

    def create(self, word_id, lang_code, pos_code, definition, example, category_id=None, author_id=None):
        sql = '''INSERT INTO Definition (word_id, lang_code, pos_code, definition, example, created_at, category_id, author_id)
                 VALUES (%s, %s, %s, %s, %s, NOW(), %s, %s)'''
        vals = (word_id, lang_code, pos_code, definition, example, category_id, author_id)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, vals)
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating word: {e}")
            return None
        #finally:
        #    cursor.close()

    def read_all(self):
        sql = 'SELECT * FROM Definition ORDER BY word_id'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def read_one(self, definition_id):
        sql = 'SELECT * FROM Definition WHERE definition_id = %s'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (definition_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def update_one(self, definition_id, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = %s")
            values.append(value)
        if not fields:
            print("No fields to update.")
            return False
        sql = f"UPDATE Definition SET {', '.join(fields)} WHERE definition_id = %s"
        values.append(definition_id)
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

    def delete_one(self, definition_id):
        sql = 'DELETE FROM Definition WHERE definition_id = %s'
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (definition_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting word: {e}")
            return False
        #finally:
        #    cursor.close()

    def delete_all(self):
        sql = 'DELETE FROM Definition'
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

    def read_by_word_id(self, word_id):
        sql = 'SELECT * FROM Definition WHERE word_id = %s'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (word_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def read_by_lang_pos_and_definition(self, lang_code, pos_code, definition):
        sql = 'SELECT * FROM Definition WHERE lang_code = %s AND pos_code = %s AND definition = %s'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (lang_code, pos_code, definition))
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()