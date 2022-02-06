import json

import sqlite3
from sqlite3 import Error


class Retrieve_Post_Cl():

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
            "SELECT post_code,post_class,post_heading,post_description,post_file_name,post_date,post_file_exten,post_comments FROM posts_cvs WHERE post_class=?", (self.class_code,))
        rows = self.cursor.fetchall()
        for ix in rows:
            temp = dict(ix)
            temp["post_comments"] = json.loads(temp["post_comments"])
            self.post_in.append(temp)

    def fetch_class_code(self):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            self.data = json.load(settings_json_file)
            self.class_code = self.data["class_selected"]

    def write_to_json(self):
        self.data["posts_in_class"] = self.post_in
        with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
            json.dump(self.data, settings_json_file, indent=4)

    def __init__(self):
        self.post_in = []
        self.create_connection()
        self.fetch_class_code()
        self.ret()
        self.write_to_json()

