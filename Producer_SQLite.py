import sqlite3

def create_table():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        task TEXT NOT NULL,
        status TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO tasks (task, status) VALUES (?, 'pending')
    ''', (task,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    task = "Rozmowa telefoniczna"
    add_task(task)
    print(f"Zadanie '{task}' zostało dodane do bazy danych.")