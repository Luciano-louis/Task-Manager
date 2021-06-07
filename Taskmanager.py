from datetime import date

access = False
current_user = ""

#set conditions to loop if invalid user and password is given and allow access if correct details is submitted
while access == False:
    with open('user.txt', 'r+') as user_file:
        username = input("Please enter your name: ")
        password = input("Please enter your password: ")
        username = username.strip()
        password = password.strip()

        for line in user_file.readlines():
            line = line.strip()
            login_credentials = line.split(", ")

            if username == login_credentials[0] and password == login_credentials[1]:
                access = True

    if access == False:
        print("Invalid user and password")
#set menu
if access == True:
    current_user = username
    print(f"welcome {username}")
    print("Please select one of the following options: ")
    if username == "admin": #set for only admin
        print("r - register user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit")
    if username == "admin": #set for only admin
        print("s - statistics")
    selection = input("")

# create condition to append new passwords
if selection == "r":
    if username == "admin":
        new_password = input("please enter new user and password (user, password): ")
        with open('user.txt', 'a') as f:
            f.write('\n' + new_password) #writes new password
        print("New user and password has been added to 'user.txt'.")
elif selection == "a":
    new_task = input(
        "please enter the username of the person the task is assigned to, the title of the task, the description of the task, the due date of the task: \n")
    new_task = new_task.split(", ")
    n_assigned_to = (new_task[0])
    n_task = (new_task[1])
    n_task_description = (new_task[2])
    n_due_date = (new_task[3])
    n_date_assigned = str(date.today())
    n_completion = "No" #adds new task

    with open('tasks.txt', 'a') as f2:
        f2.write(f"\n{n_assigned_to}, {n_task}, {n_task_description}, {n_date_assigned}, {n_due_date}, {n_completion}")
        print("New task has been added to 'tasks.txt'.")

# view current tasks
elif selection == "va":
    source = open('tasks.txt', 'r+')
    for line in source.readlines():
        line = line.split(", ")
        print("Task:\t\t\t\t" + (line[1]))
        print("Assigned to:\t\t" + (line[0]))
        print("Date assigned:\t\t" + (line[3]))
        print("Due date:\t\t\t" + (line[4]))
        print("Task complete?:\t\t" + (line[5]))
        print("Task_description: \n" + (line[2]))
        print("\n")
    source.close()

# view specific current tasks
elif selection == "vm":
    source = open('tasks.txt', 'r+')
    for line in source.readlines():
        line = line.split(", ")
        if line[0] == username: #shows tasks for specific users only
            print("Task:\t\t\t\t" + (line[1]))
            print("Assigned to:\t\t" + (line[0]))
            print("Date assigned:\t\t" + (line[3]))
            print("Due date:\t\t\t" + (line[4]))
            print("Task complete?:\t\t" + (line[5]))
            print("Task_description: \n" + (line[2]))
            print("\n")
    source.close()


if selection == "s":
    if username == "admin":
        source = open('tasks.txt', 'r+') #provides a count for users and passwords
        line_count = len(source.readlines())
        print("Amount of tasks:\t\t" + str(line_count))
        source.close()
        source = open('user.txt', 'r+')
        line_count = len(source.readlines())
        print("Amount of users:\t\t" + str(line_count))
        source.close()

else:
    exit()
#End

