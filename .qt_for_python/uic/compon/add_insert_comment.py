import json

import sqlite3
from sqlite3 import Error


class Comments():

    database = r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\college_virtual_space.db"

    def fetch_existing_comments(self):
        self.cursor.execute(
            "SELECT post_comments FROM posts_cvs WHERE post_code=?", (self.post, ))

        rows = self.cursor.fetchall()
        self.existing_comments = json.loads(rows[0][0])

    def create_connection(self):
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.database)
            # self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
        except Error as e:
            self.valid = False
            print(e)

    def insert(self):
        self.existing_comments.append(self.di)
        print(self.di)
        sql = ''' UPDATE posts_cvs SET post_comments=? WHERE post_code=?'''
        # print("dumb", json.dumps(self.existing_comments))
        json_data = json.dumps(self.existing_comments)
        self.cursor.execute(sql, (json_data, self.post))
        self.connection.commit()
        from sql.fetch_posts import Retrieve_Post_Cl
        Retrieve_Post_Cl()

    def __init__(self, post, user, comment):
        self.existing_comments = []
        self.create_connection()

        self.post = post
        self.user = user
        self.comment = comment
        self.di = {
            "user": self.user,
            "comment": self.comment
        }
        self.fetch_existing_comments()
        # print(self.existing_comments)
        


# Comments("ykkIk9neRp", "12", "123")
