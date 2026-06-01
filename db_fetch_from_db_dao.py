import sqlite3
from db_dao import get_all_students, add_student

add_student("Eve", 24, "A")
print(get_all_students())
# [{'id': 1, 'name': 'Alice', ...}, {'id': 5, 'name': 'Eve', ...}]