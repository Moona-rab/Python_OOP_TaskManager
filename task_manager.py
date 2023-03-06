#Use the following username and password to access the admin rights 
#username: admin
#password: password
#create functions for r, a, va, vm and modify
#create function for generate reports and write to file 'user_overview.txt' and 'task_overview.txt
#modify ds to display in readable format


import os
from datetime import datetime, date
from collections import Counter

#variable initialisation
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w", encoding="utf-8") as default_file:
        pass

with open("tasks.txt", 'r', encoding="utf-8") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

def reg_user():
    ''' Function for registering a new user. '''

    new_username = input("Enter username: ")
    new_password = input("Enter password: ")

    if new_username in usernames:
        print("This username already exists in the database")
    
    else:

        with open('user.txt', "a", encoding="utf-8") as f:
        
            f.write(f"\n{new_username};{new_password}")
            print("New user has been registered!")


def add_task():

    '''
        Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.


    '''
    l_users = list_users()
    usernames = l_users[0]


    while True:

        task_username = input("Name of person assigned to task: ")
        if task_username not in usernames:
            
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        
        while True:
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    break

                except ValueError:
                    print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
       
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False, 
             
        }
        # adding task to 'tasks.txt' file by using '.append' function
        task_list.append(new_task)
        with open("tasks.txt", "w", encoding="utf-8") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")
        break

def update_task(list_index):
    ''' Create a dictionary and update the 'completed' key '''
    u_task_dict = task_list[list_index]
    u_task_dict["completed"] = True
    
    with open("tasks.txt", "w", encoding="utf-8") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


def edit_task(list_index, user, due_date):
    ''' Create a dictionary and update the 'completed' key '''

    u_task_dict = task_list[list_index]
    u_task_dict["completed"] = True
    u_task_dict["username"] = user
    u_task_dict["due_date"] = due_date

    with open("tasks.txt", "w", encoding="utf-8") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    

def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
            format of Output 2 presented in the task pdf (i.e. includes spacing
            and labelling) 

    '''
    i = 0
    for t in task_list:
        i= i + 1 
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n \t\t {t['description']}\n"
        disp_str += f"Task No: \t {i}\n"
        print(disp_str)
    
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
    '''

    v=0
    task_num = []
   
    for t in task_list:
        v +=1
        if t['username'] == username:
        
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n \t\t {t['description']}\n"
            disp_str += f"Completed: \t {'Yes' if t['completed'] else 'No'}\n"
            disp_str += f"Task No: \t {v}\n"

            
            print(disp_str)
            task_num.append(v)
        
        
    while True:
    
        # ask user to input selection
        while True:
            try:
                selection = int(input("Select Task No to update or enter '-1' to return to main menu \n"))
                break
            except ValueError:
                print("Please input integer only...")  
                continue
        
        if selection == -1:
            break    

        elif selection in task_num:
   
            # variable to store the index of the list
            index = selection -1 
            
            while True:
                usr_input = input("enter c to update completed status or e to edit task ")
                
                if usr_input == "c":

                    # call update task function
                    update_task(index)
                    print(f"\n Task {selection} successfully completed.")
                    break

                if usr_input == "e":

                    while True:
                        try:
                            task_due_date = input("Due date of task (YYYY-MM-DD): ")
                            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                            e_usr_name = input("provide new username to update: ")
                            if e_usr_name not in usernames:
                                print("User does not exist. Please enter a valid username")
                                continue
                            else:
                                edit_task(index, e_usr_name, due_date_time)
                            break

                        except ValueError:
                            print("Invalid datetime format. Please use the format specified")
                    
                        

                    print(f"\n Task successfully updated.")
                    break
                else:
                    print("invalid selection")

        else:
            print("You have made a wrong choice, please try again")    
   
       
def stats():
    '''If the user is an admin they can display statistics about number of users
            and tasks.'''
    
    if username == 'admin':
         
        if os.path.exists("user_overview.txt"):
            with open("user_overview.txt", "r") as f1:
                print("----- User overview ------ \n")
                print(f1.read())
              

            if os.path.exists("task_overview.txt"):
                with open("task_overview.txt", "r") as f2:
                    print("----- Task overview ------ \n")
                    print(f2.read())
            else:
                print("file does not exist, run generate reports")    
        else:
            print("file does not exist, run generate reports")         
    else:
        print("\n Only admin can access statistics")            

def user_overview():
    '''
    ▪ The total number of users registered with task_manager.py.
    ▪ The total number of tasks that have been generated and
    tracked using task_manager.py.
    ▪ For each user also describe:
    ▪ The total number of tasks assigned to that user.
    ▪ The percentage of the total number of tasks that have
    been assigned to that user
    ▪ The percentage of the tasks assigned to that user that
    have been completed
    ▪ The percentage of the tasks assigned to that user that
    must still be completed
    ▪ The percentage of the tasks assigned to that user that
    have not yet been completed and are overdue
    '''

    num_users = len(usernames)
    num_tasks = len(task_list)
    
    usr_file_str =  f"Number of users: \t\t {num_users} \n"
    usr_file_str += f"Number of tasks: \t\t {num_tasks} \n"
       
    for u in usernames:
        
        usr_file_str += f"\n user: \t {u} \n"
        usr_task_count = 0
        usr_completed_task = 0
        usr_overdue = 0
        
        for t in task_list:
            if t['username'] == u:
                usr_task_count += 1
                
                if t['completed'] == True:
                    usr_completed_task += 1 

                if t['completed'] == False and t['due_date'] < datetime.now():
                    usr_overdue += 1        

                usr_task_percent = round(usr_task_count / num_tasks * 100)
                usr_completed_task_percent = round(usr_completed_task / usr_task_count * 100)
                usr_incompleted_task_percent = round(100 - usr_completed_task_percent)
                usr_overdue_percent = round(usr_overdue / usr_task_count * 100)


        usr_file_str += f"\t user task count: \t {usr_task_count} \n"
        usr_file_str += f"\t user task percent:\t {usr_task_percent} \n"
        usr_file_str += f"\t % tasks completed:\t {usr_completed_task_percent} \n"
        usr_file_str += f"\t % tasks remaining:\t {usr_incompleted_task_percent} \n"
        usr_file_str += f"\t % tasks overdue: \t {usr_overdue_percent} \n"

   
    # Create user_overview.txt if it doesn't exist 
    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as task_o:
            pass
    # write content to file
    with open("user_overview.txt", "w") as f:
        f.write(usr_file_str)


def task_overview():
    '''
        ▪ The total number of tasks that have been generated and
        tracked using the task_manager.py.
        ▪ The total number of completed tasks.
        ▪ The total number of uncompleted tasks.
        ▪ The total number of tasks that haven’t been completed and
        that are overdue.
        ▪ The percentage of tasks that are incomplete.
        ▪ The percentage of tasks that are overdue.
    '''
    # Total number of tasks in the task list
    num_tasks = len(task_list)
    
    # The total number of completed tasks.
    completed_tasks = 0
    for t in task_list:
        if t['completed'] == True:
           completed_tasks += 1

    # The total number of uncompleted tasks.
    incompleted_tasks =  num_tasks - completed_tasks 
    
    # The total number of tasks that haven’t been completed and that are overdue.
    overdue = 0
    for t in task_list:
        if t['completed'] == False and t['due_date'] < datetime.now():
           overdue += 1   
           
    # The percentage of tasks that are incomplete.
    incomplete_percent = round(incompleted_tasks / num_tasks * 100)

    # The percentage of tasks that are overdue.
    overdue_percent = round(overdue / num_tasks * 100)

    #put all data into a string appender
    file_str = f"Number of tasks: {num_tasks}\n"
    file_str += f"Number of completed tasks: {completed_tasks}\n"
    file_str += f"Number of incomplete tasks: {incompleted_tasks}\n"
    file_str += f"Number of overdue tasks: {overdue}\n"
    file_str += f"The percentage of tasks that are incomplete: {incomplete_percent}\n"
    file_str += f"The percentage of tasks that are overdue: {overdue_percent}\n"
   
    
    # Create task_overview.txt if it doesn't exist 
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as task_o:
            pass
    # write content to file
    with open("task_overview.txt", "w") as f:
        f.write(file_str)


def generate_reports():
    '''
        ▪ The total number of tasks that have been generated and
        tracked using the task_manager.py.
        ▪ The total number of completed tasks.
        ▪ The total number of uncompleted tasks.
        ▪ The total number of tasks that haven’t been completed and
        that are overdue.
        ▪ The percentage of tasks that are incomplete.
        ▪ The percentage of tasks that are overdue.
    '''
    task_overview() 
    user_overview()
    print("\nReports have been generated!")



def list_users():
    '''accesssing registered usernames and passwords from text file 'user.txt'''

    usernames = []
    passwords = []

    with open ('user.txt', 'r') as f:

        for lines in f:

            temp = lines.strip() # removing the line space
            temp = temp.split(';') # creating list using ';' to split string into items

            usernames.append(temp[0])
            passwords.append(temp[1])

    return usernames, passwords;

l_users = list_users()
l_pwd = list_users()

usernames = l_users[0]
passwords = l_pwd[1]

logged_in = False

while not logged_in:

    username = input("Username: ").lower() # removing case sensitivity for username input
    password = input("Password: ")
    
    if username not in usernames:
        print("Incorrect username. Try again.")
    
    elif password not in passwords:
        print("Incorrect password. Try again.")
        
    else:
        print("\n") # adding line break for visual clarity
        print(f"Welcome {username}, please select one of the following options:")
        logged_in = True # breaking out of while loop

while logged_in:

    menu = input('''

r - Register a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':

        reg_user()

    elif menu == 'a':

        add_task()
    
    elif menu == 'va':

        view_all()

    elif menu == 'vm':

        view_mine()
        

    elif menu == 'ds': 
        
        stats()

    elif menu == 'gr': 
        
        generate_reports()    


    elif menu == 'e':
        
        print("Goodbye!")
        exit()

    else:
        print("You have made a wrong choice, please try again")