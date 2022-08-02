import os
import mariadb
import sqlite3
from notes import note, db_backend


def create_connection(name='my_database'):
    conn = None

    if db_backend == 'mariadb':
        try:
            conn = mariadb.connect(
                user="root",
                password=os.environ.get("DB_ROOT_PWD"),
                host="mariadb",
                port=3306,
                database=name
            )
            conn.auto_reconnect = True
        except Exception as e:
            note.logger.error("Error: cannot connect to db - %s" % e)
            return

    elif db_backend == 'local':
        try:
            conn = sqlite3.connect(name + ".db")
        except Exception as e:
            note.logger.error("Error: cannot connect to db - %s" % e)
            return

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        note.logger.error("Error: cannot create table - %s" % e)

    conn.close()

def drop_table(conn, drop_table_sql):
    try:
        c = conn.cursor()
        c.execute(drop_table_sql)
    except Exception as e:
        note.logger.error("Error: cannot drop table - %s" % e)

    conn.close()

def create_note(conn, notes):
    query = "INSERT  INTO notes(data) VALUES(?)"
    cur = conn.cursor()

    try:
        note.logger.info("Adding Note %s", notes)
        cur.execute(query, notes)
    except Exception as e:
        note.logger.error("Error: cannot create note - %s" % e)

    lastRowId = cur.lastrowid
    conn.commit()
    conn.close()

    return lastRowId


def delete_note(conn, id):
    query = 'DELETE FROM notes WHERE id=?'
    cur = conn.cursor()

    try:
        note.logger.info("Deleteing Note #%s", id)
        cur.execute(query, (id,))
    except Exception as e:
        note.logger.error("Error: cannot delete note - %s" % e)

    conn.commit()
    conn.close()

def select_note_by_id(conn, id=None):
    query = "SELECT * FROM notes"
    cur = conn.cursor()

    if id:
        query = query + " WHERE id = '%s'" % id

    try:
        note.logger.info("Getting all notes!")
        cur.execute(query)
    except Exception as e:
        note.logger.error("Error: cannot select note by id - %s" % e)

    allItems = cur.fetchall()
    conn.close()
    return allItems
