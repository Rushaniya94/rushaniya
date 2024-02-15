
import tkinter as tk
import sqlite3

conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT,
                 content TEXT)''')
conn.commit()


def add_note():
    title = entry_title.get()
    content = text_content.get("1.0", tk.END)
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    entry_title.delete(0, tk.END)
    text_content.delete("1.0", tk.END)


root = tk.Tk()
root.title("Notes")


label_title = tk.Label(root, text="Title:")
label_title.pack()
entry_title = tk.Entry(root)
entry_title.pack()


label_content = tk.Label(root, text="Content:")
label_content.pack()
text_content = tk.Text(root)
text_content.pack()


button_add = tk.Button(root, text="Add the note", command=add_note)
button_add.pack()

root.mainloop()

conn.close()
