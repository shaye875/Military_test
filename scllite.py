import sqlite3
def create_db_add_conected():
    conn = sqlite3.connect("placement.db")
    conn.row_factory = sqlite3.Row
    return conn
