import sqlite3

def get_user(username):
    db = sqlite3.connect("example.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    # This line below is vulnerable to SQL Injection
    db.execute(query)
    db.close()
