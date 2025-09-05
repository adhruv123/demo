hello dhruv
def save_tasks():
    """
    Save all tasks currently displayed in the GUI listbox to the TASKS_FILE and notify the user.
    
    Writes each entry from the global `listbox` (indices 0 through tk.END) as a separate line to the file path given by the global `TASKS_FILE`. After successfully writing the file, displays an informational message box confirming the save. Any I/O errors will propagate to the caller.
    """
    with open(TASKS_FILE, "w") as f:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def add_task():
    """
    Add the current text from the entry widget to the listbox.
    
    If the entry contains non-empty text, insert it at the end of the listbox and clear the entry widget. If the entry is empty, show a warning message box prompting the user to enter a task.
    
    Side effects:
    - Mutates the GUI: inserts an item into `listbox` and clears `entry`.
    - May display a warning dialog via `messagebox`.
    """
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
