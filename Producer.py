import csv
import uuid

FILE_PATH = "C:/Users/domin/Desktop/Zaawansowane Programowanie/Zadanie_zajecia.txt"

def create_task():
    task_id = str(uuid.uuid4())
    task_status = "pending"
    task_description = "Rozmowa telefoniczna"

    with open(FILE_PATH, mode="a") as file:
        file.write(f"{task_id},{task_status},{task_description}\n")
    print(f"Nowe zadanie zostało dodane: {task_id}")

if __name__ == "__main__":
    create_task()