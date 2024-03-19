# function to add tasks
def add_task():
    tasks.append(input("Enter your task"))
    save_tasks()

#function to remove tasks
def remove_task():
    print(tasks)
    item_index = int(input("\n which item do you want to remove"))
    del tasks[item_index]
    save_tasks()

#function to view tasks
def view_task():
    for item in tasks:
        print(item)

#  function to save tasks to tasks.txt file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# copying tasks.txt file content to the list tasks, making tasks an empty list upon receiving an error.
try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []

# continuosly prompting the user for input
while True:
    print("\n what do you want to do?")
    print("1. add a task")
    print("2. remove a task")
    print("3. view the tasks")
    print("4. exit")

    user_choice = int(input("Enter your choice"))

    if user_choice == 1:
        add_task()
    elif user_choice == 2:
        remove_task()
    elif user_choice == 3:
        view_task()
    elif user_choice == 4:
        print("Exiting the program")
        break
    else:
        print("Invalid choice")