'''
Data structures with python CA-2 Project.
Program to implement a to-do list where user can add, remove
& set prority to tasks using list data structure.
'''

# Creating a class which will contain all the methods.
class To_Do_List :

    # Creating a constructor to create an empty list.
    def __init__(self):
        self.tasks = []
    
    # Defining the add function.
    def add_task(self, task, priority):
        self.tasks.append((task, priority))
        # Acknowledging the user if the task is added successfully or not.
        print(f"Task '{task}' with Priority '{priority}' added to the to-do list.")

    # Defining the remove function.
    def remove_task(self, task, priority):
        task_to_remove = (task, priority)
        if task_to_remove in self.tasks:
            self.tasks.remove(task_to_remove)
            # Acknowledging the user that the task is successfully removed.
            print(f"Task '{task}' with Priority '{priority}' is removed from to-do list.")

        # Printing a message if the task to be removed is not present in the to-do list.
        else:
            print(f"Task '{task}' with Priority '{priority}' is not present in the to-do list.")
    
    # Creating a function for displaying tasks.
    def display_task(self):
        # Printing a message if there are no tasks present in the to-do list.
        if not self.tasks:
            print("No tasks in the to-do list.")

        # Displaying the tasks in the to-do list.
        else:
            print("Tasks in the to-do list: ")
            priority_order={"high": 1, "medium": 2, "low": 3}
            sorted_tasks = sorted(self.tasks, key=lambda task: (priority_order[task[1].lower()], task[0])) # The sorted method with lambda function will help print tasks in terms of their priority.
            for index, (task, priority) in enumerate(sorted_tasks, start=1):
                print(f"{index}. Priority: {priority}, Task: {task}")


# Creating a To-do list.
my_todo_list = To_Do_List()

# Defining functions for each choice.

def add_task_action():
    task = input("Enter the task: ") 
    # Creating to variable to store the priority of the task.

    priority = input("Enter the priority (high, medium, low): ").lower() # The lower() function will give the flexibility to the user to give the priority value in Uppercase too.
    
    # Storing the values of task and priority in order to validate both values at the same time.
    is_valid_task = not task.isdigit()
    is_valid_priority = priority in ["high", "medium", "low"]
    
    # Checking the values for task and priority and pass respective the message if the value is Invalid.
    if is_valid_task and is_valid_priority:
        my_todo_list.add_task(task, priority)
    elif not is_valid_task and not is_valid_priority:
        print("Invalid \"task\" input. A \"task\" cannot be just numbers.")
        print("Invalid \"priority\" input. A \"priority\" should be set to high, medium, or low.")
    elif not is_valid_task:
        print("Invalid \"task\" input. A \"task\" cannot be just numbers.")
    else:
        print("Invalid \"priority\" input. \"priority\" should be set to high, medium or low.")

def remove_task_action():
    task = input("Enter the task to remove: ")
    priority = input("Enter the priority of the task that has to be removed: ").lower()
    my_todo_list.remove_task(task, priority)

def display_tasks_action():
    my_todo_list.display_task()

def exit_program_action():
    print("Exiting the program")
    quit()

# Creating a dictionary for storing the actions.
menu = {
    "1": add_task_action,
    "2": remove_task_action,
    "3": display_tasks_action,
    "4": exit_program_action
}

# Printing the menu for the user.
while True: 
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    # Storing the choice of the user in a variable.
    choice = input("Enter your choice: ")

    if choice in menu:
        menu[choice]()
    else: 
        print("Invalid choice. Please select a valid option.")

'''
Data structures with python CA-2 Project.
Program to implement a to-do list where user can add, remove
& set prority to tasks using list data structure.
'''

# Creating a class which will contain all the methods.
class To_Do_List :

    # Creating a constructor to create an empty list.
    def __init__(self):
        self.tasks = []
    
    # Defining the add function.
    def add_task(self, task, priority):
        self.tasks.append((task, priority))
        # Acknowledging the user if the task is added successfully or not.
        print(f"Task '{task}' with Priority '{priority}' added to the to-do list.")

    # Defining the remove function.
    def remove_task(self, task, priority):
        task_to_remove = (task, priority)
        if task_to_remove in self.tasks:
            self.tasks.remove(task_to_remove)
            # Acknowledging the user that the task is successfully removed.
            print(f"Task '{task}' with Priority '{priority}' is removed from to-do list.")

        # Printing a message if the task to be removed is not present in the to-do list.
        else:
            print(f"Task '{task}' with Priority '{priority}' is not present in the to-do list.")
    
    # Creating a function for displaying tasks.
    def display_task(self):
        # Printing a message if there are no tasks present in the to-do list.
        if not self.tasks:
            print("No tasks in the to-do list.")

        # Displaying the tasks in the to-do list.
        else:
            print("Tasks in the to-do list: ")
            priority_order={"high": 1, "medium": 2, "low": 3}
            sorted_tasks = sorted(self.tasks, key=lambda task: (priority_order[task[1].lower()], task[0])) # The sorted method with lambda function will help print tasks in terms of their priority.
            for index, (task, priority) in enumerate(sorted_tasks, start=1):
                print(f"{index}. Priority: {priority}, Task: {task}")


# Creating a To-do list.
my_todo_list = To_Do_List()

# Defining functions for each choice.

def add_task_action():
    task = input("Enter the task: ") 
    # Creating to variable to store the priority of the task.

    priority = input("Enter the priority (high, medium, low): ").lower() # The lower() function will give the flexibility to the user to give the priority value in Uppercase too.
    
    # Storing the values of task and priority in order to validate both values at the same time.
    is_valid_task = not task.isdigit()
    is_valid_priority = priority in ["high", "medium", "low"]
    
    # Checking the values for task and priority and pass respective the message if the value is Invalid.
    if is_valid_task and is_valid_priority:
        my_todo_list.add_task(task, priority)
    elif not is_valid_task and not is_valid_priority:
        print("Invalid \"task\" input. A \"task\" cannot be just numbers.")
        print("Invalid \"priority\" input. A \"priority\" should be set to high, medium, or low.")
    elif not is_valid_task:
        print("Invalid \"task\" input. A \"task\" cannot be just numbers.")
    else:
        print("Invalid \"priority\" input. \"priority\" should be set to high, medium or low.")

def remove_task_action():
    task = input("Enter the task to remove: ")
    priority = input("Enter the priority of the task that has to be removed: ").lower()
    my_todo_list.remove_task(task, priority)

def display_tasks_action():
    my_todo_list.display_task()

def exit_program_action():
    print("Exiting the program")
    quit()

# Creating a dictionary for storing the actions.
menu = {
    "1": add_task_action,
    "2": remove_task_action,
    "3": display_tasks_action,
    "4": exit_program_action
}

# Printing the menu for the user.
while True: 
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    # Storing the choice of the user in a variable.
    choice = input("Enter your choice: ")

    if choice in menu:
        menu[choice]()
    else: 
        print("Invalid choice. Please select a valid option.")

