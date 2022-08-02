import os

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash

note = Flask(__name__)
note.config.from_object(Config)
bootstrap = Bootstrap(note)
auth = HTTPBasicAuth()
db_backend = os.environ.get("NOTES_DB_BACKEND", "local")

users = {
    "admin": generate_password_hash("yeet")
}

from notes import db, routes

sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            data TEXT);"""

if db_backend == 'mariadb':
    sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                                id INTEGER NOT NULL AUTO_INCREMENT,
                                data TEXT,
                                PRIMARY KEY (id));"""

conn = db.create_connection()

if conn is not None:
    db.create_table(conn, sql_create_notes_table)
else:
    note.logger.error("Error! cannot create the database connection.")
