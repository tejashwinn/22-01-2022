import random
import json
from datetime import datetime

import sqlite3
from sqlite3 import Error


class Sub_Assignment():

    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

    def to_binary(self):
        try:
            with open(self.file_path, 'rb') as file:
                blobData = file.read()
            self.file = blobData
            self.valid = True
        except:
            self.valid = False
            self.errors = "Invalid File"

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            self.valid = False
            print(e)

    def submission(self):
        # print(self.di)
        self.to_binary()
        if self.valid:
            sql = ''' INSERT INTO as_sub_cvs(
                as_code,
                as_user,
                as_last_date,
                as_sub_date,
                as_max_marks,
                as_file,
                as_file_name,
                as_exten)
                VALUES(?,?,?,?,?,?,?,?) '''
                
            self.cursor.execute(sql, [
                self.as_code,
                self.username,
                self.last_date,
                self.sub_date,
                self.maxmarks,
                self.file,
                self.file_name,
                self.file_extension
            ]
            )
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            self.valid = True
            self.errors = ''

    def fetch_as_code(self):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            self.as_code = str(data["as_selected"])
            self.username = str(data["log"]["username"])
            self.valid=True
            self.errors=""
    def __init__(self, cur_date, di, file_path=""):

        self.file_path = file_path
        self.file_name = file_path.split('/')[-1]
        self.file_extension = file_path.split('/')[-1].split('.')[-1]
        self.di = di
        self.sub_date = cur_date
        self.last_date = self.di["as_sub_date"].rsplit(":", 1)[0]
        self.valid = False
        self.errors = ""
        self.maxmarks = di["as_marks"]
        self.create_connection()
        self.fetch_as_code()
