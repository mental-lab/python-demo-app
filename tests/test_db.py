import os
import time
import unittest
import notes
from notes import db


class TestDB(unittest.TestCase):

    def setUp(self):
        self.db_name = "test_database"
        self.conn = db.create_connection(name=self.db_name)

    def tearDown(self):
        pass

    def test_create_table(self):
        db.create_table(self.conn, notes.sql_create_notes_table)

        conn = db.create_connection(name=self.db_name)
        res = conn.execute("SELECT name FROM sqlite_schema WHERE type='table';")
        nameExists = False
        for name in res:
            if "'notes'," in str(name):
                nameExists = True

        self.assertTrue(nameExists, "Test failed, couldn't find database table 'test'")
