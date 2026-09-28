import sqlite3

class Database:
   def __init__(self,db_name):
       self.con = sqlite3.connect(db_name)
       self.cur = self.con.cursor()
       self.create_table("shipments")
       self.insert_data()
       
   def create_table(self,name:str):
        self.cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {name}(
            id INTEGER PRIMARY KEY,
            Content TEXT,
            weight REAL,
            status TEXT
        )
            """
        )
        self.con.commit()


def insert_data(self):
        self.cur.execute("""
        INSERT INTO {name} (
        id INTEGER PRIMARY KEY,
          content TEXT,
        weight REAL,
        status TEXT,
        )
    """)

db = Database("supply.db")

           

