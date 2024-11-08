tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({'task': task, 'completed': False})
    print("Task added!")

def view_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i}. {task['task']} - {status}")

def complete_task():
    view_tasks()
    task_num = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['completed'] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

main()
