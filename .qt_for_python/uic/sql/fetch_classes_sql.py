import json
import sqlite3
from sqlite3 import Error


class Fetch_Classes_Cl():
    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

    def json_data(self):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            self.username = data["log"]["username"]

    def create_connection(self, js=False):
        self.connection = None
        self.cursor = None

        try:
            self.connection = sqlite3.connect(self.database)
            if js:
                # This enables column access by name: row['column_name']
                self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
        except Error as e:
            print(e)

    def check_for_admin(self):
        self.cursor.execute(
            "SELECT class_name,class_description,class_code,class_admin,class_students FROM classes_cvs WHERE class_admin=?", (self.username,))
        rows = self.cursor.fetchall()
        for ix in rows:
            temp = dict(ix)
            temp["class_students"] = json.loads(temp["class_students"])
            self.owned_classes.append(temp)

    def check_for_joined(self):
        self.cursor.execute(
            "SELECT class_code,class_students FROM classes_cvs")
        rows_all = self.cursor.fetchall()
        classes = [
            rows_all[i][0]
            for i in range(len(rows_all))
            if self.username in json.loads(rows_all[i][1])
        ]

        self.create_connection(js=True)
        for i in classes:
            self.cursor.execute(
                "SELECT class_name,class_description,class_code,class_admin,class_students FROM classes_cvs WHERE class_code=?", (i,))
            rows = self.cursor.fetchall()
            temp = dict(rows[0])
            temp["class_students"] = json.loads(temp["class_students"])
            self.joined_classes.append(temp)

    def write_classes_owned_to_json(self):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            data["classes_owned"] = self.owned_classes
            data["classes_joined"] = self.joined_classes

        with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
            json.dump(data, settings_json_file, indent=4)
            # print(json.dumps(data, indent=4))

    def __init__(self):
        self.owned_classes = []
        self.joined_classes = []
        self.json_data()
        if self.username != "":
            self.create_connection(js=True)
            self.check_for_admin()
            self.create_connection()
            self.check_for_joined()
        else:
            self.owned_classes = []
            self.joined_classes = []
        self.write_classes_owned_to_json()


Fetch_Classes_Cl()
