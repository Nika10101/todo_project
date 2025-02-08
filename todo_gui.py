import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

app = tk.Tk()
app.title("To-Do List")

frame = tk.Frame(app)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=50)
task_entry.pack(side=tk.LEFT, padx=10)

add_task_button = tk.Button(frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(app, width=60, height=15)
task_listbox.pack(pady=10)

remove_task_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_task_button.pack()

app.mainloop()