'''import tkinter as tk
def on_pressed (event):
    text= entry.get()
    label.config(text= "Enter pushed. Text:"+text)

window=tk.Tk()
window.geometry("400x400")

entry=tk.Entry(window)
entry.pack()
entry.bind("<Return>",on_pressed)


label= tk.Label(window,text="")
label.pack()


window.mainloop()'''

import tkinter as tk

def closeWindow():
    label.configure(text="New text")
window= tk.Tk()
window.title("testing window")
window.geometry("600x300")
label= tk.Label(window, text="This is the 20th lecture", font=("Arial",12), bg="green")
label.config(bd=20, bg='#ffaaaa')
btn= tk.Button(command='clear')
def delete_button():
    btn=tk.Button(text="Click",command=delete_button)


btn.pack()
label.pack()
window.mainloop()