from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Получаем переменные окружения
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT", "5432")

try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
    """)
    conn.commit()
except Exception as e:
    print("Не удалось подключиться к БД:", e)
    conn = None
    cur = None

@app.route('/api/notes', methods=['GET'])
def get_notes():
    if conn is None:
        return jsonify({"error": "Нет соединения с базой данных"}), 500
    try:
        cur.execute("SELECT id, title, content FROM notes ORDER BY id DESC")
        rows = cur.fetchall()
        notes = [{'id': r[0], 'title': r[1], 'content': r[2]} for r in rows]
        return jsonify(notes)
    except Exception as e:
        return jsonify({"error": f"Ошибка при получении данных: {e}"}), 500

@app.route('/api/notes', methods=['POST'])
def add_note():
    if conn is None:
        return jsonify({"error": "Нет соединения с базой данных"}), 500
    try:
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
    except Exception as e:
        return jsonify({"error": f"Ошибка при добавлении заметки: {e}"}), 500

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    if conn is None:
        return jsonify({"error": "Нет соединения с базой данных"}), 500
    try:
        cur.execute("DELETE FROM notes WHERE id = %s RETURNING id", (note_id,))
        deleted = cur.fetchone()
        conn.commit()
        if deleted:
            return jsonify({"message": f"Заметка с id {note_id} удалена"}), 200
        else:
            return jsonify({"error": f"Заметка с id {note_id} не найдена"}), 404
    except Exception as e:
        return jsonify({"error": f"Ошибка при удалении заметки: {e}"}), 500

@app.route('/api/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    if conn is None:
        return jsonify({"error": "Нет соединения с базой данных"}), 500
    try:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        cur.execute(
            "UPDATE notes SET title = %s, content = %s WHERE id = %s RETURNING id",
            (title, content, note_id)
        )
        updated = cur.fetchone()
        conn.commit()
        if updated:
            return jsonify({"message": f"Заметка с id {note_id} обновлена"}), 200
        else:
            return jsonify({"error": f"Заметка с id {note_id} не найдена"}), 404
    except Exception as e:
        return jsonify({"error": f"Ошибка при обновлении заметки: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

