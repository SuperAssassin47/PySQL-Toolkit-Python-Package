import sqlite3

def init_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Employees ("
                   "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "Name TEXT NOT NULL,"
                   "Email TEXT NOT NULL,"
                   "Phone INTEGER NOT NULL,"
                   "Employment_Status BOOLEAN NOT NULL,"
                   "Other TEXT NOT NULL,"
                   "Notes TEXT"
                   ")")

    conn.commit()
    conn.close()
