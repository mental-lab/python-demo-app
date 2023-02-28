import os
import logging
import sqlite3
from sqlite3 import Error


def create_connection(name='notes.db'):
    conn = None

    try:
        conn = sqlite3.connect(name)
    except Error as e:
        logging.error(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_note(conn, notes):
    query = "INSERT INTO notes(data) VALUES(?)"

    c = conn.cursor()
    c.execute(query, notes)
    c.commit()

    return c.lastrowid


def delete_note(conn, id):
    query = 'DELETE FROM notes WHERE id=?'
    
    c = conn.cursor()
    c.execute(query, (id,))
    c.commit()
    
    conn.commit()

def select_note_by_id(conn, id=None):
    query = "SELECT * FROM notes"

    if id:
        query = query + " WHERE id = '%s'" % id

    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    return rows
