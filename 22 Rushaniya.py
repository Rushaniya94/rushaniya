import tkinter as tk 

def bold():
    text.tag_add("bold",text.index(tk.SEL_FIRST), text.index(tk.SEL_LAST))
    text.tag_config("bold", font=("Times New Roman",14,"bold"))
window=tk.Tk()
window.title("The main window")
text=tk.Text(window, height=30, width=50)
text.pack()
button=tk.Button(window, text="Make thetext bold",command=bold)
def button_click():
    label.config(text="Exit!")
def toggle():
    if var.get():
        label.config(text="Push the button")
    else:
        label.config(text="The button is already pushed")
var=tk.BooleanVar()
checkbox=tk.Checkbutton(text="ON", variable=var,command=toggle)
checkbox.pack()
def show_text():
    entered_text=entry.get()
    label.config(text=f"You entered the text")
    
root= tk.Tk()
root.title("Welcome!")
label=tk.Label(root, text="My name is Ru.", font=("Arial",18), fg="dark grey", bg="turquoise", justify="left")
label.pack()
button= tk.Button(root,text="Are You sure, You want to exit??")
command= button_click
button.pack()
label=tk.Label(root, text="")
root.mainloop()