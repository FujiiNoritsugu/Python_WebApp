import os

db_path = 'sqlite:///test_db'
if not os.path.exists('test_db'):
    print("Database file not found.")
else:
    print("Database file found.")
