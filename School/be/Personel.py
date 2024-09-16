import sqlite3 as sqlite

def UP():
    connection = sqlite.connect('database.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS User_pass (
                  UserPass_id INTEGER PRIMARY KEY,
                  User_name TEXT,
                  Pass_name TEXT
                  )""")
    connection.commit()

    connection.close()