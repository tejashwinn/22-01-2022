import sqlite3
from sqlite3 import Error


class Sign_In_Check():

    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(e)

    def __init__(self, email_id, password):
        self.database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"
        self.create_connection()
        self.name = ""
        self.username = ""
        self.email_id = email_id
        import hasher
        temp = hasher.Password_Hasher(password)
        self.password = temp.hashed_password
        self.check_credentials()

    def check_credentials(self):
        self.cursor.execute(
            "SELECT name,username,emailid FROM users_cvs WHERE emailid=? and password=?", (self.email_id, self.password,))
        rows = self.cursor.fetchall()
        self.credentials_exists = rows != []
        if self.credentials_exists:
            (self.name, self.username, self.email_id) = rows[0]
            self.password = None
        else:
            (self.name, self.username, self.email_id,
             self.password) = ("", "", "", "")
