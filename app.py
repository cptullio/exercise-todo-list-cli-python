todos = []
stop = False

def get_todos():
    return todos

def add_one_task(title):
    todos.append(title)

def print_list():
    print(todos)

def delete_task(number_to_delete):
    del todos[int(number_to_delete)-1]

def save_todos():
    file = open('todos.csv', 'w+') # open the file for writing 'w', create if it doesn't exists
    for item in todos:
        file.write(item + '\n')
    file.close() # close the file

    
def load_todos():
    todos.clear()
    with open('todos.csv') as file:
        for line in file.readlines():
            todos.append(line.strip('\n'))

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")