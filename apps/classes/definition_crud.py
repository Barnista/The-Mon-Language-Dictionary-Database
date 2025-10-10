import mysql.connector
from mysql.connector import Error

class DefinitionCRUD:
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

    def create(self, word_id, language_id, pos_id, definition, example, category_id=None):
        sql = '''INSERT INTO Definition (word_id, language_id, pos_id, definition, example, created_at, category_id)
                 VALUES (%s, %s, %s, %s, %s, NOW(), %s)'''
        vals = (word_id, language_id, pos_id, definition, example, category_id)
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
        sql = 'SELECT * FROM Definition'
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
