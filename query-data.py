import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Fetch ALL rows
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("All students:")
for row in rows:
    print(row)

# Fetch ONE row
cursor.execute("SELECT * FROM students WHERE name = ?", ("Alice",))
student = cursor.fetchone()
print("\nFound student:", student)

# Fetch with condition
cursor.execute("SELECT * FROM students WHERE grade = ?", ("A",))
top_students = cursor.fetchall()
print("\nGrade A students:", top_students)

conn.close()