import os
import time
import unittest
import notes
from notes import db


class TestDB(unittest.TestCase):

    def setUp(self):
        self.db_name = "my_database"
        self.conn = db.create_connection()

    def tearDown(self):
        pass

    def test_create_table(self):
        
        try:
            db.create_table(self.conn, notes.sql_create_notes_table)
            nameExists = True
        except: 
            nameExists = False

        self.assertTrue(nameExists, "Test failed, couldn't find database table 'test'")

