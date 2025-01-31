from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
    conn.commit()
    conn.close()

def add_user(name, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, hashed_password))
    conn.commit()
    conn.close()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    add_user(data["name"], data["password"])
    return "Usuario registrado"

if __name__ == "__main__":
    create_db()
    app.run(port=7890)
