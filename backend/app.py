from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Get environment variables
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT", "5432")

# Debug: print DB config (you can remove this after deployment)
print("Connecting to DB with:")
print("DB_NAME:", db_name)
print("DB_USER:", db_user)
print("DB_HOST:", db_host)
print("DB_PORT:", db_port)

# Connect to RDS PostgreSQL
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
""")
conn.commit()

@app.route('/api/notes', methods=['GET'])
def get_notes():
    cur.execute("SELECT id, title, content FROM notes")
    rows = cur.fetchall()
    notes = [{'id': r[0], 'title': r[1], 'content': r[2]} for r in rows]
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    cur.execute(
        "INSERT INTO notes (title, content) VALUES (%s, %s) RETURNING id",
        (title, content)
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    return jsonify({'id': new_id, 'title': title, 'content': content}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

