import sqlite3

conn = sqlite3.connect("collection.db")

cursor = conn.cursor()

cursor.execute("CREATE TABLE asset(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT NOT NULL)")
cursor.execute("CREATE TABLE task(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT NOT NULL)")
cursor.execute("CREATE TABLE worker(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL, phone TEXT NOT NULL)")
cursor.execute("CREATE TABLE allocatetask(id INTEGER PRIMARY KEY AUTOINCREMENT, aid INT NOT NULL, tid INT NOT NULL, wid INT NOT NULL, toa DATE NOT NULL, etc DATE NOT NULL)")

conn.commit()

conn.close()
