# Program: To-Do List with Priority Listing
# to-do list structured as a dictionary to store tasks as keys and the priority listing as values (1 to 3)
# ex. "Clean my room: High Priority (3)"
# use loop to print tasks in order by priority: 3 = High to 1 = Low
# tasks will be loaded and saved to a file

import json
from json.decoder import JSONDecodeError

tasks = {}

# load keys and values from tasks.json
def load_tasks():
    """Load keys and values from tasks.json"""
    global tasks
    print("Loading tasks...")
    with open("tasks.json") as f:
        try:
            task_list = json.load(f)
            tasks = task_list
            f.close()
            print("Loaded all tasks!\n")
            display_tasks()
        except JSONDecodeError:
            print("There are no tasks to load.\n")

def display_tasks():
    print("Here are your current tasks:\n")
    print("High Priority:")
    for task, priority in tasks.items():
        if tasks[task] == '3':
            print(f"{task}: High Priority ({priority})")
    print("\nMedium Priority:")
    for task, priority in tasks.items():
        if tasks[task] == '2':
            print(f"{task}: Medium Priority ({priority})")
    print("\nLow Priority:")
    for task, priority in tasks.items():
        if tasks[task] == '1':
            print(f"{task}: Low Priority ({priority})")
            
def add_task():
    new_task = input("Enter a new task to the list:\n> ")
    new_task_priority = input("Enter a priority value: ('3' - High, '2' - Medium, '1' - Low)\n> ")
    if new_task_priority == '':
        print("That task priority value is invalid. Please try again.\n")
        return
    if int(new_task_priority) > 3:
        print("That task priority value is invalid. Please try again.\n")
        return
    tasks[new_task] = new_task_priority
    if tasks[new_task] == '3':
        print(f"You have added: {new_task}\nWith a priority of: High\n")
    elif tasks[new_task] == '2':
        print(f"You have added: {new_task}\nWith a priority of: Medium\n")
    else:
        print(f"You have added: {new_task}\nWith a priority of: Low\n")

def mark_as_complete():
    completed_task = input("Choose a task to mark as complete:\n> ")
    if completed_task in tasks:
            del tasks[completed_task]
            print("Task deleted!")

def save_tasks():
    print("Saving tasks...")
    with open("tasks.json", "w") as f:
            json.dump(tasks, f)
            f.close()
            print("Saved all tasks!")

def menu():
    while True:
        action = input("""What would you like to do?
        
1: Mark task as completed
2: Add new task
3: Display tasks
4: Save task list
5: Exit

> """)
        if action == '1':
            if not tasks:
                print("There are currently no tasks.\n")
                menu()
            mark_as_complete()
        if action == '2':
            add_task()
        if action == '3':
            if not tasks:
                print("There are currently no tasks.\n")
                menu()
            display_tasks()
        if action == '4':
            if not tasks:
                print("There are currently no tasks.\n")
                menu()
            save_tasks()
        if action == '5':
            exit()

def main():
    print("-" * 20 + " To-Do List " + "-" * 20)
    load_tasks()
    menu() # Goes straight to menu of there are no tasks found by load_tasks()

if __name__ == "__main__":
    main()