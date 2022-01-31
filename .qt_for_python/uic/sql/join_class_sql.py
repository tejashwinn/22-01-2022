import sqlite3
from sqlite3 import Error
import json


class Join_Classes_Cl():
    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(e)

    def json_data(self):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            self.username = data["log"]["username"]

    def check_for_class(self):
        self.cursor.execute(
            "SELECT * FROM classes_cvs WHERE class_code=?", (self.class_code,))
        rows = self.cursor.fetchall()
        if rows == []:
            self.valid = False
            self.errors = "Invalid Class Code try again"
        else:
            self.valid = True
            self.errors = ""

    def check_for_owner(self):
        self.cursor.execute(
            "SELECT class_admin FROM classes_cvs WHERE class_code=? and class_admin=?", (self.class_code, self.username))
        rows = self.cursor.fetchall()
        # print(rows)
        if rows != []:
            # print(1)
            self.Valid = False
            #error
            #error
            #error
            #error
            #error
            #error
            #error
            #error
            #error
            #gives true instead of false to change
            # print(self.valid)
            self.errors = "Can't join class which you had created"
        else:
            # print(2)
            self.Valid = True
            self.errors = ""

    def check_for_already_joined_class(self):
        self.cursor.execute(
            "SELECT class_students FROM classes_cvs WHERE class_code=?", (self.class_code, ))

        rows = self.cursor.fetchall()
        rows = rows[0][0]
        rows = json.loads(rows)
        self.existing_students = rows.copy()
        # print(self.existing_students)
        # print(self.valid)

        if str(self.username) not in self.existing_students:
            self.valid = True
            self.errors = ""
        else:
            self.valid = False
            self.errors = "Already joined class"

    def join(self):
        if self.valid and self.errors == "":
            self.existing_students.append(str(self.username))

            sql = ''' UPDATE classes_cvs SET class_students=? WHERE class_code=?'''
            # print("dumb", json.dumps(self.existing_students))
            json_data = json.dumps(self.existing_students)
            self.cursor.execute(sql, (json_data, self.class_code))
            self.connection.commit()

    def __init__(self, class_code):
        self.class_code = class_code
        self.errors = ""
        self.existing_students = []
        self.create_connection()
        self.json_data()
        self.check_for_class()

        if self.valid and self.errors == "":
            self.check_for_owner()
        if self.valid and self.errors == "":
            self.check_for_already_joined_class()
