import tkinter as tk
from tkinter import messagebox, ttk


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.tasks = []  # List to store tasks

        # Title Label
        title_label = tk.Label(self.root, text="Task Manager", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Task:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.task_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=1, padx=5)
        
        add_button = tk.Button(input_frame, text="Add Task", font=("Arial", 12), bg="green", fg="white", command=self.add_task)
        add_button.grid(row=0, column=2, padx=5)

        # Task List Frame
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10)

        self.task_list = ttk.Treeview(list_frame, columns=("Task", "Status"), show="headings", height=10)
        self.task_list.heading("Task", text="Task")
        self.task_list.heading("Status", text="Status")
        self.task_list.column("Task", width=350)
        self.task_list.column("Status", width=150)
        self.task_list.pack(side="left")

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.task_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.task_list.config(yscrollcommand=scrollbar.set)

        # Button Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        remove_button = tk.Button(button_frame, text="Remove Task", font=("Arial", 12), bg="red", fg="white", command=self.remove_task)
        remove_button.grid(row=0, column=0, padx=10)

        complete_button = tk.Button(button_frame, text="Mark as Completed", font=("Arial", 12), bg="blue", fg="white", command=self.mark_completed)
        complete_button.grid(row=0, column=1, padx=10)

        sort_button = tk.Button(button_frame, text="Sort Tasks", font=("Arial", 12), bg="purple", fg="white", command=self.sort_tasks)
        sort_button.grid(row=0, column=2, padx=10)

    def add_task(self):
        """Add a new task to the list."""
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Input Error", "Task cannot be empty!")
            return
        if any(t[0] == task for t in self.tasks):
            messagebox.showwarning("Duplicate Task", "This task already exists!")
            return

        self.tasks.append((task, "Pending"))
        self.task_entry.delete(0, tk.END)
        self.update_task_list()

    def remove_task(self):
        """Remove the selected task from the list."""
        selected_item = self.task_list.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No task selected!")
            return
        
        for item in selected_item:
            task_name = self.task_list.item(item, "values")[0]
            self.tasks = [t for t in self.tasks if t[0] != task_name]
        self.update_task_list()

    def mark_completed(self):
        """Mark the selected task as completed."""
        selected_item = self.task_list.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No task selected!")
            return
        
        for item in selected_item:
            task_name = self.task_list.item(item, "values")[0]
            self.tasks = [(t[0], "Completed") if t[0] == task_name else t for t in self.tasks]
        self.update_task_list()

    def sort_tasks(self):
        """Sort tasks alphabetically and by completion status."""
        self.tasks.sort(key=lambda x: (x[1], x[0]))
        self.update_task_list()

    def update_task_list(self):
        """Update the displayed task list."""
        for item in self.task_list.get_children():
            self.task_list.delete(item)

        for task, status in self.tasks:
            self.task_list.insert("", tk.END, values=(task, status))


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
