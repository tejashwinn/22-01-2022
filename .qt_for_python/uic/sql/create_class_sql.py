import random
import sqlite3
from sqlite3 import Error


class Create_Classes():
    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    def random_generator(self):
        self.random_name = "".join(random.choice(self.chars)
                                   for _ in range(10))

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(e)

    def json_data(self):
        import json
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            self.username = data["log"]["username"]

    def check_for_code(self):
        self.cursor.execute(
            "SELECT class_code FROM classes_cvs WHERE class_code=?", (self.random_name,))
        rows = self.cursor.fetchall()
        if rows != []:
            self.random_generator()
            self.check_for_code()

    def check_for_same_class_name(self):
        self.cursor.execute(
            "SELECT * FROM classes_cvs WHERE class_name=? and class_admin=?", (self.name, self.username))
        rows = self.cursor.fetchall()
        self.valid = rows == []

    def insert(self):
        sql = ''' INSERT INTO classes_cvs(class_name,class_description,class_code,class_admin)
              VALUES(?,?,?,?) '''
        self.cursor.execute(
            sql, [self.name, self.description, self.random_name, self.username, ])
        self.connection.commit()
        from sql.fetch_classes_sql import Fetch_Classes_Cl
        Fetch_Classes_Cl

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.create_connection()
        self.random_generator()
        self.check_for_code()
        self.json_data()
        self.check_for_same_class_name()
