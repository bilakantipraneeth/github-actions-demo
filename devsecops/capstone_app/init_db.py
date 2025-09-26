import sqlite3
import os

# Delete the old database file if it exists
if os.path.exists('database.db'):
    os.remove('database.db')

connection = sqlite3.connect('database.db')

sql_script = """
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);
INSERT INTO users (username, email) VALUES ('alice', 'alice@example.com');
INSERT INTO users (username, email) VALUES ('bob', 'bob@example.com');
"""

connection.executescript(sql_script)
connection.commit()
connection.close()
print("Database initialized with two users.")
