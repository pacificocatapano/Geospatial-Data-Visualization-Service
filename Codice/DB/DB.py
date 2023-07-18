import sqlite3

def initDB():
    connection = sqlite3.connect('Codice/DB/sqlite.db')
    with open('./DB/sqlite.sql') as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()

def connectDB():
    connection = sqlite3.connect('Codice/DB/sqlite.db')
    connection.row_factory = sqlite3.Row
    return connection
