import tkinter as tk
from tkinter import messagebox
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")
def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
app = tk.Tk()
app.title("To-Do List")
tasks_listbox = tk.Listbox(app)
tasks_listbox.pack(pady=10)
task_entry = tk.Entry(app)
task_entry.pack(pady=10)
add_button = tk.Button(app, text="Add Task", command=add_task)
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
add_button.pack(pady=5)
remove_button.pack(pady=5)
save_button = tk.Button(app, text="Save Tasks", command=save_tasks)
save_button.pack(pady=5)
try:
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            tasks_listbox.insert(tk.END, task.strip())
except FileNotFoundError:
    pass
app.mainloop()
