import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# DANGEROUS: Hardcoded secret
app.config['SECRET_KEY'] = 'super-secret-key-that-should-not-be-in-code'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    # DANGEROUS: SQL Injection vulnerability
    user_id = request.args.get('id')
    conn = get_db_connection()
    if user_id:
        # This is the vulnerable part
        users = conn.execute("SELECT * FROM users WHERE id = '" + user_id + "'").fetchall()
    else:
        users = conn.execute('SELECT * FROM users').fetchall()
    
    conn.close()
    return jsonify([dict(ix) for ix in users])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
