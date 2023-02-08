import os

import sqlite3
from flask import g

DATABASE = os.getenv("SQL_DB_PATH")


def get_db():
    db = getattr(g, '_database', None)
    print("Connected to DB")
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
