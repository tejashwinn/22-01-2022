from sql.fetch_events import Retrieve_Events_Cl
import random
import json

import sqlite3
from sqlite3 import Error

from datetime import datetime


class Create_Event_cl():

    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    def random_generator(self):
        self.random_name = "".join(random.choice(self.chars)
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

    def insert(self):
        sql = ''' INSERT INTO events_cvs(ev_code,ev_heading,ev_description,ev_date)
              VALUES(?,?,?,?) '''
        self.cursor.execute(
            sql,  [self.random_name, self.name, self.description, self.date])
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        Retrieve_Events_Cl()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.date = str(datetime.now())
        self.create_connection()
        self.random_generator()
