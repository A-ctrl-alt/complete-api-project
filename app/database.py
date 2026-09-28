import sqlite3

connection = sqlite3.connect("sql.db")

cur=connection.cursor()
#to insert data


cur.execute(
"""
CREATE TABLE  IF NOT EXISTS shipment(
    id INTEGER,
    weight REAL,
    content TEXT,
    status TEXT
    )
"""
)


# cur.execute("""INSERT INTO shipment VALUES(1272,2.5,"laptop","placed")""")
# cur.execute("""INSERT INTO shipment VALUES(1273,3.0,"book","shipped")""")
# cur.execute("""INSERT INTO shipment VALUES(1274,1.5,"phone","delivered")""")


#to fetch data
cur.execute("""
SELECT * FROM shipment
""" )

data = cur.fetchall()
print(data)


#fetch data for specific id
id = 1273
cur.execute(
"""
    SELECT  FROM shipment WHERE id=?
"""(id)
)
data = cur.fetchone()
print(data)

connection.commit()

connection.close()










