class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append({'task': task, 'completed': False})
        print('task added successfully')

    def view_task(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Not Done"
                print('{}. {} --> {}'.format(index, task['task'], status))

        else:
            print('No task found in the list')

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print('Task Completed Successfully')
        else:
            print("Invalid task index")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task {} deleted Successfully".format(task_index))
        else:
            print("Invalid task index")


def main():
    todolist = TodoList()

    while True:
        print('''Enter a choice:
        1. Add a task
        2. View tasks
        3. Mark task completed
        4. Delete task
        5. Exit''')
        choice = int(input("Enter a choice: "))
        if choice == 1:
            todolist.add_task()
        elif choice == 2:
            todolist.view_task()
        elif choice == 3:
            task_index = int(input("Enter the index of the task to be marked completed: "))
            todolist.mark_completed(task_index)
        elif choice == 4:
            task_index = int(input("Enter the index of the task to be deleted: "))
            todolist.delete_task(task_index)
        elif choice == 5:
            print('Exiting...')
            break
        else:
            print("Invalid Choice Entered\nPlease Try again!!!")


if __name__ == "__main__":
    main()
