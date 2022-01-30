import sqlite3
from sqlite3 import Error


class Sign_Up_Insert():
    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(e)

    def __init__(self, name, username, email_id, password):
        self.name = name
        self.username = username
        self.email_id = email_id
        self.password = password
        
        self.create_connection()
        self.unique_username()
        self.unique_emailid()

    def insert(self):
        from hasher import Password_Hasher
        self.password = Password_Hasher(self.password).hashed_password
        sql = ''' INSERT INTO users_cvs(name,username,emailid,password)
              VALUES(?,?,?,?) '''
        self.cursor.execute(
            sql, [self.name, self.username, self.email_id, self.password])
        self.connection.commit()
        # return self.cursor.lastrowid

    def unique_username(self):
        self.cursor.execute(
            "SELECT username FROM users_cvs WHERE username=?", (self.username,))
        rows = self.cursor.fetchall()
        self.unique_username_constraint = rows == []

    def unique_emailid(self):
        self.cursor.execute(
            "SELECT emailid FROM users_cvs WHERE emailid=?", (self.email_id,))
        rows = self.cursor.fetchall()
        self.unique_emailid_constraint = rows == []

