import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Updated Name", 1))
conn.commit()

print("Record updated successfully")

cursor.close()
conn.close()
