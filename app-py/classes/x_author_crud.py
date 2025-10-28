import mysql.connector
from mysql.connector import Error

class XAuthorCRUD:
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

    def create_with_id(self, id, name, bio=None):
        sql = '''INSERT INTO Author (id, name, bio)
                 VALUES (%s, %s, %s)'''
        vals = (id, name, bio)
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

    def create(self, name, bio=None):
        sql = '''INSERT INTO Author (name, bio)
                 VALUES (%s, %s)'''
        vals = (name, bio)
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
        sql = '''SELECT * FROM Author'''
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def read_one(self, author_id):
        sql = '''SELECT * FROM Author WHERE id = %s'''
        vals = (author_id)
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(sql, vals)
            return cursor.fetchone()
        except Error as e:
            print(f"Error reading word: {e}")
            return None
        #finally:
        #    cursor.close()

    def update_one(self, author_id, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = %s")
            values.append(value)
        if not fields:
            print("No fields to update.")
            return False
        sql = f"UPDATE Author SET {', '.join(fields)} WHERE id = %s"
        values.append(author_id)
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

    def delete_one(self, author_id):
        sql = '''DELETE FROM Author WHERE id = %s'''
        vals = (author_id)
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
        sql = '''DELETE FROM Author'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting words: {e}")
            return False
        #finally:
        #    cursor.close()
