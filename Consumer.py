import time

FILE_PATH = "C:/Users/domin/Desktop/Zaawansowane Programowanie/Zadanie_zajecia.txt"

def process_task(task_id):
    print(f"Praca {task_id} w toku...")
    time.sleep(30)
    print(f"Praca {task_id} zakończona!")

def update_task_status(task_id, new_status):
    tasks = []
    with open(FILE_PATH, mode="r") as file:
        for line in file:
            task_id_in_file, status, description = line.strip().split(",")
            if task_id_in_file == task_id:
                tasks.append(f"{task_id_in_file},{new_status},{description}\n")
            else:
                tasks.append(line)

    with open(FILE_PATH, mode="w") as file:
        file.writelines(tasks)

def consume_tasks():
    while True:
        try:
            with open(FILE_PATH, mode="r") as file:
                for line in file:
                    task_id, status, description = line.strip().split(",")
                    if status == "pending":
                        update_task_status(task_id, "in_progress")
                        process_task(task_id)
                        update_task_status(task_id, "done")
        except FileNotFoundError:
            print("Brak pliku z zadaniami. Oczekiwanie na nowe zadania...")
        time.sleep(5)


if __name__ == "__main__":
    consume_tasks()