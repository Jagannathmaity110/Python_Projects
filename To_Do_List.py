tasks = []

def view_task():
    for i,task in enumerate(tasks,1):  #enumerate function in used for iterate over a loop
        print(f"{i}.{task}")

def add_task(task):
    tasks.append(task)

def remove_task(index):
    tasks.pop(index-1)


while True :
    action = input("Choose an action [add, view , remove ,quit]").lower()
    if action  == "add":
        task = input("Enter the taks :")
        add_task(task)
    elif action == "view":
        view_task()
    elif action == "remove":
        index = int(input("Enter the task number to remove : "))
        remove_task(index)
    elif action == "quit":
        break