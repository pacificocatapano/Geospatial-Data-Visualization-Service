import sqlite3

def initDB():
    connection = sqlite3.connect('./DB/sqlite.db')
    #cursor = connection.cursor()
    #cursor.execute(f'DELETE FROM Utenti;')
    with open('./DB/sqlite.sql') as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()

def connectDB():
    connection = sqlite3.connect('./DB/sqlite.db')
    connection.row_factory = sqlite3.Row
    return connection
