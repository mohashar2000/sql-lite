import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Insert a single row
cursor.execute("""
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
""", ("Alice", 20, "A"))

# Insert multiple rows at once
students = [
    ("Bob", 22, "B"),
    ("Charlie", 21, "A"),
    ("Diana", 23, "C"),
]
cursor.executemany("""
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
""", students)

conn.commit()
print("✅ Data inserted!")

conn.close()