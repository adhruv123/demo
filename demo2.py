hello dhruv
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
