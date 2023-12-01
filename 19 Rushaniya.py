import tkinter as tk

window= tk.Tk()
window.title("testing window")
window.geometry("600x300")
label= tk.Label(window, text="Good morning. My name is Rushaniya and I am 29. I am from KZ and live in Almaty", font=("Arial",12))
label.config(bd=20, bg='#ffaaaa')
btn= tk.Button(text="Nice to meet You!")
def click_button():
    global clicks
    clicks+=1
    btn["Good bye"]=f"Clicks{clicks}"
btn.pack()
label.pack()
window.mainloop()