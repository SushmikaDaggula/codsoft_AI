'''this helps to users to organize their tasks efficiently
and also allows users to create, update, and track their to-do lists'''
import os

class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_as_done(self):
        self.done = True

    def __str__(self):
        status = "[Done]" if self.done else "[Todo]"
        return f"{status} {self.description}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_as_done(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_as_done()
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet.")

    def save_tasks_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.description}\n")

    def load_tasks_from_file(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                task_descriptions = file.readlines()
                self.tasks = [Task(description.strip()) for description in task_descriptions]

def display_menu():
    print("Todo List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

def main():
    todo_list = TodoList()
    todo_list.load_tasks_from_file()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            description = input("Enter task description: ")
            todo_list.add_task(description)
            print("Task added successfully.")
        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter task number to mark as done: "))
            todo_list.mark_task_as_done(task_number)
        elif choice == "4":
            todo_list.save_tasks_to_file()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
