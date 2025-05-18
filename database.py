import sqlite3

def connect_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            contact TEXT,
            department TEXT,
            semester TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert(name, email, contact, department, semester):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student (name, email, contact, department, semester) VALUES (?, ?, ?, ?, ?)",
                   (name, email, contact, department, semester))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

def update(student_id, name, email, contact, department, semester):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE student SET name=?, email=?, contact=?, department=?, semester=? WHERE id=?
    """, (name, email, contact, department, semester, student_id))
    conn.commit()
    conn.close()
