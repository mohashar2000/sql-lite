import sqlite3

# Connect to DB (creates "school.db" file if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
""")

conn.commit()
print("✅ Database and table created!")

conn.close()