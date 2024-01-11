'''import tkinter as tk

def on_checkbox():
    if var.get()==1:
        res_label.config(text="button is clicked")
    else:
        res_label.config(text="button is not clicked")
        

root=tk.Tk()
root.title ("Main window")
var=tk.IntVar()
checkbutt=tk.Checkbutton(root, text="Push", variable=var, command= on_checkbox)
checkbutt.pack()

res_label=tk.Label(root, text="")
res_label.pack()
root.mainloop()'''

import tkinter as tk

from tkinter import ttk

def on_pressed(event):
    text=entry.get()
    label.config(text="Hello "+text+"!!! \n To clean the dialog put on\n 'Clean'")

def delete():
    text=entry.get()
    label.config(text="You pushed the button CLEAN  ")
    entry.delete(0, tk.END)


def on_canvas_click(event):
    x,y = event.x,event.y
    print(f"Click ({x},{y})")

root=tk.Tk()
root.geometry("400x200")

root.title("    Welcome     ")

listbox = ["one", "seecond", "third"]
combobox = ttk.Combobox(root,values = listbox)
label=tk.Label(root, text="To greet yourself write down your name:\n  and then push ENTER")
label.pack()
combobox.pack()

entry=tk.Entry(root, width='100')
entry.pack()
entry.bind("<Return>", on_pressed)

button=tk.Button(root,text="Clean", command=delete)
button.pack()

canvas=tk.Canvas(root,width=400,height=200)
canvas.pack()
canvas.create_oval(50,0,20,30, fill="yellow")


canvas.bind("<Button-1>",on_canvas_click)

root.mainloop()
