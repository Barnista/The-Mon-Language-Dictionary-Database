import mysql.connector
from mysql.connector import Error

class WordCRUD:
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

    def create_word(self, word, pronunciation, language_id, created_at):
        sql = '''INSERT INTO Word (word, pronunciation, language_id, created_at)
                 VALUES (%s, %s, %s, NOW())'''
        vals = (word, pronunciation, language_id, created_at)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, vals)
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating word: {e}")
            return None
        finally:
            cursor.close()

    def read_all_word(self):
        sql = 'SELECT * FROM Word ORDER BY word ASC'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchone()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        finally:
            cursor.close()

    def read_word(self, word_id):
        sql = 'SELECT * FROM Word WHERE word_id = %s'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (word_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        finally:
            cursor.close()

    def update_word(self, word_id, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = %s")
            values.append(value)
        if not fields:
            print("No fields to update.")
            return False
        sql = f"UPDATE Word SET {', '.join(fields)} WHERE word_id = %s"
        values.append(word_id)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, tuple(values))
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error updating word: {e}")
            return False
        finally:
            cursor.close()

    def delete_word(self, word_id):
        sql = 'DELETE FROM Word WHERE word_id = %s'
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (word_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting word: {e}")
            return False
        finally:
            cursor.close()
