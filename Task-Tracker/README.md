# Task Tracker CLI

A simple Command Line Interface (CLI) application written in Python to track and manage your daily tasks. Tasks are automatically saved and maintained in a JSON database (`tasks.json`).

---

## Features

- **Add** new tasks with default `todo` status.
- **Update** existing task descriptions.
- **Delete** tasks (automatically re-indexes IDs to maintain sequential order).
- **Mark Status** of tasks as `in-progress` or `done`.
- **List** all tasks or filter them by status (`todo`, `in-progress`, `done`).
- Automatic timestamping (`createdAt` and `updatedAt`).

---

## Requirements

- Python 3.x

---

## Usage

Run all commands through the terminal using the following structure:

```bash
python main.py task-cli <command> [arguments]
```

### 1. Add a Task

Add a new task with a description.

```bash
python main.py task-cli add "Buy groceries"
```

### 2. Update Task Description

Update the description of an existing task by its ID.

```bash
python main.py task-cli update 1 "Buy groceries and cooked meals"
```

### 3. Delete a Task

Delete a task by its ID.

```bash
python main.py task-cli delete 1
```

### 4. Mark Task Status

Change the status of a specific task.

* **Mark as In-Progress:**
```bash
python main.py task-cli mark-in-progress 1
```


* **Mark as Done:**
```bash
python main.py task-cli mark-done 1
```



### 5. List Tasks

Display saved tasks from `tasks.json`.

* **List all tasks:**
```bash
python main.py task-cli list
```


* **List tasks with "todo" status:**
```bash
python main.py task-cli list-todo
```


* **List tasks with "in-progress" status:**
```bash
python main.py task-cli list-in-progress
```


* **List tasks with "done" status:**
```bash
python main.py task-cli list-done
```


---

## Data Format

Tasks are stored in `tasks.json` in the following structure:

```json
{
    "1": {
        "createdAt": "2026-10-05 21:00:00.000000",
        "description": "Buy groceries",
        "status": "todo",
        "updatedAt": "2026-10-05 21:00:00.000000"
    }
}

```
