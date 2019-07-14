import sqlite3

conn = sqlite3.connect("collection.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM asset")
data = cursor.fetchall()

print("Assets")
print(data)

cursor.execute("SELECT * FROM task")
data = cursor.fetchall()

print("Tasks")
print(data)

cursor.execute("SELECT * FROM worker")
data = cursor.fetchall()

print("Workers")
print(data)

cursor.execute("SELECT * FROM allocatetask")
data = cursor.fetchall()

print("Allocated Tasks")
print(data)

conn.close()
