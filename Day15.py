class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"{status} {self.title}: {self.description}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.mark_as_completed()

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")


def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
            print("Task added successfully.")
        elif choice == "2":
            todo_list.show_tasks()
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(task_index)
            print("Task removed successfully.")
        elif choice == "3":
            todo_list.show_tasks()
            task_index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(task_index)
            print("Task marked as completed.")
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
