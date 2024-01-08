import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("TO-DO List")
root.geometry("500x450+600+300")
root.config(bg="grey")

values=["1. Working", "2. Jogging", "3. Shopping","4. Studing"]

selected_value= tk.StringVar()
combobox= ttk.Combobox(root, textvariable=selected_value, values=values)
combobox.pack()

button= tk.Button(root, text="Show the selected item", command= exit)
button.pack()

menu= tk.Menu(root)
menu.add_command(label="Welcome", command= root.grid)
menu.add_command(label="Good bye", command=root.quit)
root.config(menu=menu)
root.mainloop()
