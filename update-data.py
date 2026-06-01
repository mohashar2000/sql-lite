import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# UPDATE
cursor.execute("""
    UPDATE students SET grade = ? WHERE name = ?
""", ("A+", "Bob"))
print("✅ Updated Bob's grade")

# DELETE
cursor.execute("DELETE FROM students WHERE name = ?", ("Diana",))
print("✅ Deleted Diana")

conn.commit()
conn.close()