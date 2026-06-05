tasks =[]
marked_tasks=[]
priorities=("low","mid","high")
categories=set()

def list_tasks():
    user_list=input(">tasks themselves(1) or completed tasks?(2): ")
    if user_list=="1":
        if not tasks:
            print(">>>no tasks yet")
        else:
            for number, ntask in enumerate(tasks, start=1):
                print(f"{number}.{ntask}")
    if user_list=="2":
        if not marked_tasks:
            print(">>>no completed tasks yet")
        else:
            for number, nctask in enumerate(marked_tasks, start=1):
                print(f"{number}.{nctask}")

def create_task():
    add_task=input(">whats your task?: ")
    priority=input(">whats your priority?(low,mid,high): ")
    category=input(">whats your category?: ")

    #add task
    while len(add_task)>50:
        print(">>>too much lines make it shorter")
        add_task=input(">whats your task?: ")

    #prority
    while priority not in priorities:
        print("priority not found")
        priority=input(">whats your priority?(low,mid,high): ")

    #category
    while len(category) >50:
        print(">>>too much characters make it shorter")
        category=input(">whats your category?: ")
    else:
        categories.add(category)

    if add_task and priority and category:
        print(">>>task added")

    task = {
        "id": len(tasks) + 1,
        "title": add_task,
        "priority": priority,
        "category": category,
        "completed": False,
    }
    tasks.append(task)


def mark_task():
    try:
        mark = int(input(">whats your task? enter in order , task 1 = 1: "))
        task=tasks.pop(mark-1)
        task["completed"]=True
        marked_tasks.append(task)
        print(f">>>task marked")
        if not task["completed"]:
            status = ">>>not completed"

    except ValueError:
        print(">>>enter a valid task number")
    except IndexError:
        print(">>>task number not found")

def delete_task():
    try:
        if not tasks:
            print(">>>no tasks yet")
        else:
            d = int(input(">enter the task number you want to delete: "))
            deleted_task = tasks.pop(d-1)
            print(f">>>task deleted")
    except ValueError:
        print(">>>enter a valid task number")
    except IndexError:
        print(">>>task number not found")

def search_task():
    all_t = tasks+marked_tasks
    s=input(">enter the task you want to search: ").lower()
    for stask in all_t:
        if s in all_t :
            if s == stask:
                print(f">>>result:\t{stask}")
        else:
            print(">>>task not found")


menu=("1.list tasks\t"
   "2.create task\t"
   "3.mark a task as complete\t"
   "4.delete task\t"
   "5.search for task\t"
   "6.EXIT\t"
   )

def user_nav():
    while True:
        print(menu)
        user_task=input("Enter your task number: ")
        if user_task=="1":
            list_tasks()
        if user_task=="2":
            create_task()
        if user_task=="3":
            mark_task()
        if user_task=="4":
            delete_task()
        if user_task=="5":
            search_task()
        if user_task=="6":
            exit()

user_nav()


