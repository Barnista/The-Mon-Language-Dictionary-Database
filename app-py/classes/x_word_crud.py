import mysql.connector
from mysql.connector import Error

class XWordCRUD:
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

    def create_with_id(self, id, word, ipa, th, lang_code, author_id, synonym_word_id=None):
        sql = '''INSERT INTO Word (id, word, ipa, th, lang_code, author_id, synonym_word_id, created_at)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())'''
        vals = (id, word, ipa, th, lang_code, author_id, synonym_word_id)
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

    def create(self, word, ipa, th, lang_code, author_id, synonym_word_id=None):
        sql = '''INSERT INTO Word (word, ipa, th, lang_code, created_at, author_id, synonym_word_id)
                 VALUES (%s, %s, %s, %s, NOW(), %s, %s)'''
        vals = (word, ipa, th, lang_code, author_id, synonym_word_id)
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

    def read_all(self):
        sql = 'SELECT * FROM Word ORDER BY id'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def read_with_limit(self, start_id, end_id):
        sql = 'SELECT * FROM Word WHERE id >= %s AND id <= %s ORDER BY id'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (start_id, end_id))
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def read_one(self, word_id):
        sql = 'SELECT * FROM Word WHERE id = %s'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (word_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        finally:
            cursor.close()

    def read_by_word(self, word):
        sql = 'SELECT * FROM Word WHERE word = %s'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (word,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        finally:
            cursor.close()

    def read_by_word_and_ipa(self, word, ipa):
        sql = 'SELECT * FROM Word WHERE word = %s AND ipa = %s'
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (word, ipa))
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        finally:
            cursor.close()

    def update_one(self, word_id, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = %s")
            values.append(value)
        if not fields:
            print("No fields to update.")
            return False
        sql = f"UPDATE Word SET {', '.join(fields)} WHERE id = %s"
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

    def delete_one(self, word_id):
        sql = 'DELETE FROM Word WHERE id = %s'
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

    def delete_all(self):
        sql = 'DELETE FROM Word'
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error deleting words: {e}")
            return 0
        
    def read_filter_in_diacritic(self, diacritic):
        sql = 'SELECT * FROM Word WHERE word LIKE %s ORDER BY id'
        pattern = f"%{diacritic}%"
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, (pattern,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading words with diacritic: {e}")
            return None
        #finally:
        #    cursor.close()

    def update_filter_in_diacritic(self, diacritic, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = %s")
            values.append(value)
        if not fields:
            print("No fields to update.")
            return 0
        sql = f"UPDATE Word SET {', '.join(fields)} WHERE word LIKE %s"
        pattern = f"%{diacritic}%"
        values.append(pattern)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, tuple(values))
            self.conn.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error updating words with diacritic: {e}")
            return 0
        finally:
            cursor.close()