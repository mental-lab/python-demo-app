import os
import time
import unittest
import notes
from notes import db


class TestDBCreate(unittest.TestCase):

    def setup(self):
        db.create_connection(name="test.db")

    def tearDown(self):
        os.remove("test.db")
    
    def test_create_table(self):
        conn = db.create_connection(name="test.db")
        db.create_table(conn, notes.sql_create_notes_table)
        time.sleep(2)
        
        res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        nameExists = False
        for name in res:
            if "'notes'," in str(name):
                nameExists = True
        
        self.assertTrue(nameExists, "Test failed, couldn't find database table 'notes'")
