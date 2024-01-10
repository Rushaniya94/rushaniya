import tkinter as tk 


def closeWindow ():
    jacob.configure(text = "Новый текст")

def canvas_click (event):
    x, y = event.x , event.y
    jacob.configure( text = f"Click on {x},{y}" )

window = tk.Tk()
window.title("First window")
window.geometry ("800x600")

troi = tk.Canvas(window, width=300, height=300, bg= '#9dc1b4')
lucy = tk.Button(window, text="Стереть текст")
from tkinter import *
from tkinter import messagebox
def newtask():
    task= my_entry.get()
    if task !="":
        lb.insert (END, task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("Please write the task correctly")

def deletetask():
    lb.delete (ANCHOR)

ws= Tk()
ws.geometry("500x450")
ws.config(bg="blue")

