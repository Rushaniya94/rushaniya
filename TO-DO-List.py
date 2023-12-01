
import datetime
tasks=[]
def add_task():
    task=input("Enter the task")
    tasks.append(task)
    print("The task was added in TO-DO-List")

def view_tasks():
    if tasks:
        print("To-do List")
        for i in enumerate (tasks,start=1):
            print(f"{i},{tasks}")
        else:
            print("Yout to-do list is empty")

def mark_completed():
    view_tasks()
    if tasks:
        task_index=int(input("Enter the task number to mark it  as completed"))
        if 0<= task_index<len(tasks):
            completed_tasks=tasks.pop(task_index)
            print(f"{completed_tasks} marked as completed")
        else:
            print("This task does not exist")
while True:
    print("\n Options")
    print("1. Add task")
    print("2.View task")
    print("3.Mark task as completed")
    print("4. Quit")
else:
    print(f"Your position is wrong")

for task in tasks:
        if task[1] == date[0] and task[2] == date[1]:
            if task[3] > 12:
                start_time = ' PM'
                task[3] -= 12
            else:
                start_time = ' AM'
            if task[3] > 12:
                end_time = ' PM'
                task[3] -= 12
            else: end_time = ' AM'
            print ('Task Name:', task[0])
            print ('Start time:', task[3], ':', task[4])
            print ('End time:')

for date in dates:
  print_tasks(tasks, date)
view_task()


    

    

