import json

import sqlite3
from sqlite3 import Error


class Retrieve_As_Cl():

    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
        except Error as e:
            self.valid = False
            print(e)

    def ret(self):
        self.cursor.execute(
            "SELECT as_code,as_class,as_heading,as_des,as_date,as_sub_date,as_marks,as_file_name,as_exten,as_comments FROM as_cvs WHERE as_class =?", (self.class_code,))
        rows = self.cursor.fetchall()
        for ix in rows:
            temp = dict(ix)
            # print(temp)
            temp["as_comments"] = json.loads(temp["as_comments"])
            
            self.as_in.append(temp)

    def fetch_class_code(self):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            self.data = json.load(settings_json_file)
            self.class_code = self.data["class_selected"]

    def write_to_json(self):
        self.data["as_in_class"] = self.as_in
        with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
            json.dump(self.data, settings_json_file, indent=4)

    def __init__(self):
        self.as_in = []
        self.create_connection()
        self.fetch_class_code()
        self.ret()
        self.write_to_json()
        from sql.fetch_sub import Retrieve_Sub_Cl
        Retrieve_As_Cl()
