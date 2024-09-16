import sqlite3 as sqlite
connection = sqlite.connect('database.db')
cursor = connection.cursor()

class Repository():
    def insert_user_pass_data(self, username, password):

        query = """INSERT INTO User_pass (User_name, Pass_name) VALUES (?, ?)"""

        try:
            cursor.execute(query, (username, password))
            connection.commit()
            print("Data inserted successfully.")
        except sqlite.Error as e:
            print(f"Error inserting data: {e}")

    def Read(self, tablename, col):
        query = ("select " + col + " from " + tablename)
        cursor.execute(query)
        return cursor.fetchall()

    def Read_Sort(self, tablename, col, field):
        query = f"SELECT {col} FROM {tablename} ORDER BY {field} ASC"
        cursor.execute(query)
        return cursor.fetchall()


    def Search(self, tablename, col, where, field):
        try:
            #print("select " + col + " from " + tablename + " where " + where + f" order by {field} ASC")
            query = f"SELECT {col} FROM {tablename} WHERE {where} ORDER BY {field} ASC"
            cursor.execute(query)
            return cursor.fetchall()

        except:
            return ()

    def default_Search(self, tablename, col, where):
        try:
            query = ("select " + col + " from " + tablename + " where " + where)
            cursor.execute(query)
            return cursor.fetchall()

        except:
            return ()

    def CreateTable(self, Variable):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Score_{Variable} (
        Scores_id INTEGER PRIMARY KEY,
        Reshte TEXT,
        Name TEXT,
        Family TEXT,
        Code_S TEXT,
        Dars TEXT,
        Score INTEGER
        )""")
        connection.commit()
        Repository.CreateTable2(self, Variable)


    def CreateTable2(self, Variable):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Personel_{Variable} (
        prs_id INTEGER PRIMARY KEY,
        prs_Name TEXT,
        prs_E TEXT,
        Family TEXT,
        Code_S TEXT,
        Dars TEXT,
        Score INTEGER
        )""")
        connection.commit()

        Repository.CreateTable3(self, Variable)


    def CreateTable3(self, Variable):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Dars_{Variable} (
        dars_id INTEGER PRIMARY KEY,
        dars_Name TEXT,
        dars_E TEXT,
        Family TEXT,
        Code_S TEXT,
        Dars TEXT,
        Score INTEGER
        )""")
        connection.commit()

        Repository.CreateTable4(self, Variable)


    def CreateTable4(self, Variable):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Teacher_{Variable} (
        Teachers_id INTEGER PRIMARY KEY,
        Name TEXT,
        Family TEXT,
        Dars TEXT,
        madrak TEXT,
        personel_code TEXT,
        National_Code TEXT
        )""")
        connection.commit()

        Repository.CreateTable5(self, Variable)


    def CreateTable5(self, Variable):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Student_{Variable} (
        std_id INTEGER PRIMARY KEY,
        Name TEXT,
        Family TEXT,
        dadName TEXT,
        National_Code TEXT,
        Date TEXT,
        Code_S TEXT,
        Reshte TEXT,
        mobile_dad TEXT,
        mobile_mother TEXT
        )""")
        connection.commit()

        Repository.CreateTable6(self, Variable)


    def CreateTable6(self, Variable):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Presentation_{Variable} (
        Std_Tch_id INTEGER PRIMARY KEY,
        Name TEXT,
        Family TEXT,
        Type TEXT,
        Date TEXT,
        day TEXT,
        res INTEGER,
        Class TEXT,
        Zang TEXT,
        Long TEXT,
        Exit_Class TEXT,
        Exit_School TEXT,
        today_hozor TEXT
        )""")
        connection.commit()


    def Insert(self, obj, Tablename, Cols):
        query = f"INSERT INTO {Tablename}{Cols} VALUES {obj}"

        cursor.execute(query)
        connection.commit()

    def delete(self,tablename,where):
        try:
            query = ("delete from " + tablename + " where " + where)
            cursor.execute(query)
            connection.commit()
            return True
        except:
            return False

    def update(self, tablename, col, where):
        try:
            #print("update " + tablename + " set " + col + " where " + where)
            query = ("update " + tablename + " set " + col + " where " + where)
            cursor.execute(query)
            connection.commit()
            return True
        except:
            return False