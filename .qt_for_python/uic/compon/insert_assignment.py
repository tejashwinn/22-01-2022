import random
import json
from datetime import datetime

import sqlite3
from sqlite3 import Error


class Create_Assignment():

    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    def to_binary(self):
        try:
            with open(self.file_path, 'rb') as file:
                blobData = file.read()
            self.file = blobData
            self.valid = True
        except:
            self.valid = False
            self.errors = "Invalid File"

    def random_generator(self):
        self.as_random_name = "".join(random.choice(self.chars)
                                      for _ in range(10))
        self.valid = True

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            self.valid = False
            print(e)

    def insert_with_file(self):
        self.to_binary()
        sql = ''' INSERT INTO as_cvs(
            as_code,
            as_class,
            as_heading,
            as_des,
            as_date,
            as_sub_date,
            as_marks,
            as_file,
            as_file_name,
            as_exten) 
            VALUES(?,?,?,?,?,?,?,?,?,?) '''
        self.cursor.execute(sql, [
            self.as_random_name,
            self.class_code,
            self.heading,
            self.description,
            self.date,
            self.sub_date,
            self.marks,
            self.file,
            self.file_name,
            self.file_extension]
        )
        self.final_pro()

    def insert(self):
        sql = ''' INSERT INTO as_cvs(
            as_code,
            as_class,
            as_heading,
            as_des,
            as_date,
            as_sub_date,
            as_marks)
              VALUES(?,?,?,?,?,?,?) '''
        self.cursor.execute(
            sql,  [self.as_random_name,
                   self.class_code,
                   self.heading,
                   self.description,
                   self.date,
                   self.sub_date,
                   self.marks])

        self.final_pro()

    def final_pro(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        self.valid = True
        self.errors = ''
        from sql.fetch_assignments import Retrieve_As_Cl
        Retrieve_As_Cl()

    def fetch_class_code(self):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            self.class_code = data["class_selected"]
            self.username = str(data["log"]["username"])

            from sql.fetch_classes_sql import Fetch_Classes_Cl
            Fetch_Classes_Cl()

            for i in data["classes_owned"]:
                if (str(i["class_admin"]) == str(self.username)) and (str(self.class_code) == str(i["class_code"])):
                    self.valid = True
                    self.errors = "Successfully Posted"
                    break
                else:
                    self.valid = False
                    self.errors = "No Admin Privilege"

    def __init__(self, head, description, sub_date, marks, file_path="", ):
        self.heading = head
        self.description = description

        self.file_path = file_path
        self.file_name = file_path.split('/')[-1]
        self.file_extension = file_path.split('/')[-1].split('.')[-1]

        self.date = str(datetime.now())
        self.sub_date = sub_date
        self.marks = marks

        self.valid = False
        self.errors = ""

        self.create_connection()
        self.random_generator()
        self.fetch_class_code()
