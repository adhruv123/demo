import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for task in f:
                listbox.insert(tk.END, task.strip())

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Selected", command=delete_task)
delete_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save Tasks", command=save_tasks)
save_btn.pack(pady=5)

load_tasks()

root.mainloop()
