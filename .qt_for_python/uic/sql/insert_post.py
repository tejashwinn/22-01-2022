import random
import json

import sqlite3
from sqlite3 import Error

from datetime import datetime


class Create_Post():

    def to_binary(self):
        try:
            with open(self.file_path, 'rb') as file:
                blobData = file.read()
            self.file = blobData
        except:
            self.valid = False
            self.errors = "Invalid File"

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
            self.valid = False
            print(e)

    def insert_with_file(self):
        self.to_binary()
        sql = ''' INSERT INTO posts_cvs(post_code,post_class,post_heading,post_description,post_file_name,post_date,post_file,post_file_exten) VALUES(?,?,?,?,?,?,?,?) '''
        self.cursor.execute(
            sql, [self.random_name, self.class_code, self.name, self.description, self.file_name, self.date, self.file, self.file_extension])
        self.final_pro()

    def insert(self):
        sql = ''' INSERT INTO posts_cvs(post_code,post_class,post_heading,post_description,post_date)
              VALUES(?,?,?,?,?) '''
        self.cursor.execute(
            sql,  [self.random_name, self.class_code, self.name, self.description, self.date])
        self.final_pro()

    # TODO Rename this here and in `insert_with_file` and `insert`
    def final_pro(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        self.valid = True
        self.errors = ''

    def fetch_class_code(self):
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            self.class_code = data["class_selected"]

    def __init__(self, name, description, file_path=""):
        self.name = name
        self.description = description
        self.file_path = file_path
        # print(file_path)
        self.file_name = file_path.split('/')[-1]
        self.file_extension = file_path.split('/')[-1].split('.')[-1]
        # self.connection()
        self.date = str(datetime.now())
        self.fetch_class_code()
        self.create_connection()
        self.random_generator()
