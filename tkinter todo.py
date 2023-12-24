from tkinter import *
from tkinter import messagebox

"""
Исправил цвет фона bg="0" на bg="white" в Listbox.
Исправил цвет текста fg="green".
Добавил в код создание и добавление кнопки "Delete task" 
Переименовал переменную list в task_list
Исправил command для кнопки "Add task"

Так же советую перевести программу то есть её вывод, и добавить реализацию от себя еще
"""
def newtask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Please write the task correctly")

def deletetask():
    lb.delete(ANCHOR)

ws = Tk()
ws.title("TO-DO List")
ws.geometry("500x450+600+300")
ws.config(bg="blue")

frame = Frame(ws)
frame.pack(pady=10)
lb = Listbox(frame, width=25, height=8, font=('Times', 16), bg="white", fg="green", selectbackground="brown")
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    "buy presents",
    "decorate the Christmas tree",
    "watch Home Alone",
    "bake cookies"
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(ws, font=("Times", 18))
my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addtask_btn = Button(button_frame, text="Add task", font=("Times", 12), bg="grey", padx=20, pady=10, command=newtask)
addtask_btn.pack()

deletetask_btn = Button(button_frame, text="Delete task", font=("Times", 12), bg="grey", padx=20, pady=10, command=deletetask)
deletetask_btn.pack()

ws.mainloop()
