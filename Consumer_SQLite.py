import sqlite3
import time

def read_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, task FROM tasks WHERE status = "pending"')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_status(task_id, new_status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE tasks SET status = ? WHERE id = ?
    ''', (new_status, task_id))
    conn.commit()
    conn.close()

def perform_task(task_id, task_name):
    print(f"Rozpoczynanie zadania: {task_name}")
    update_task_status(task_id, 'in_progress')
    time.sleep(30) 
    update_task_status(task_id, 'done')
    print(f"Zadanie zakończone: {task_name}")

if __name__ == "__main__":
    while True:
        tasks = read_tasks()
        for task_id, task_name in tasks:
            perform_task(task_id, task_name)
        time.sleep(5)
