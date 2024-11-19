# Array Personal Task Manager

## Overview

The Array Personal Task Manager is a simple task management application built using Python and Tkinter. This application allows users to add, remove, and mark tasks as completed. The tasks are stored in an array, making it easy to manage and manipulate the task list.

## Features

- **Add Task**: Add a new task to the list.
- **Remove Task**: Remove a selected task from the list.
- **Mark as Completed**: Mark a selected task as completed.
- **Sort Tasks**: Sort tasks alphabetically and by completion status.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ArrayPersonalTaskManager.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ArrayPersonalTaskManager
    ```
3. Run the application:
    ```bash
    python personalTaskManager.py
    ```

## Usage

1. **Add a Task**: Enter the task description in the input field and click the "Add Task" button. The task will be added to the list with a "Pending" status.
2. **Remove a Task**: Select a task from the list and click the "Remove Task" button. The selected task will be removed from the list.
3. **Mark as Completed**: Select a task from the list and click the "Mark as Completed" button. The status of the selected task will be changed to "Completed".
4. **Sort Tasks**: Click the "Sort Tasks" button to sort the tasks alphabetically and by their completion status.

## Code Explanation

The core functionality of the task manager is implemented using an array to store the tasks. Each task is represented as a tuple containing the task description and its status.

### Adding a Task

The `add_task` method adds a new task to the array:
```python
def add_task(self):
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
```

### Removing a Task

The `remove_task` method removes the selected task from the array:
```python
def remove_task(self):
    selected_item = self.task_list.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No task selected!")
        return
    
    for item in selected_item:
        task_name = self.task_list.item(item, "values")[0]
        self.tasks = [t for t in self.tasks if t[0] != task_name]
    self.update_task_list()
```

### Marking a Task as Completed

The `mark_completed` method updates the status of the selected task in the array:
```python
def mark_completed(self):
    selected_item = self.task_list.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No task selected!")
        return
    
    for item in selected_item:
        task_name = self.task_list.item(item, "values")[0]
        self.tasks = [(t[0], "Completed") if t[0] == task_name else t for t in self.tasks]
    self.update_task_list()
```

### Sorting Tasks

The `sort_tasks` method sorts the tasks in the array:
```python
def sort_tasks(self):
    self.tasks.sort(key=lambda x: (x[1], x[0]))
    self.update_task_list()
```

## Conclusion

The Array Personal Task Manager is a simple yet effective application for managing tasks. By using an array to store tasks, the application ensures efficient task management and manipulation. Feel free to explore and enhance the application as per your requirements.
