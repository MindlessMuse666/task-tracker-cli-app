import sys
import json
import os
from datetime import datetime


class Task:
    def __init__(self, task_id, description, status="todo", created_at=None, updated_at=None):
        self.id = task_id
        self.description = description
        self.status = status
        self.createdAt = created_at if created_at else datetime.now()
        self.updatedAt = updated_at if updated_at else datetime.now()

    def mark_progress(self):
        self.status = "in-progress"
        self.updatedAt = datetime.now()

    def mark_done(self):
        self.status = "done"
        self.updatedAt = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data["id"],
            description=data["description"],
            status=data["status"],
            created_at=datetime.fromisoformat(data["createdAt"]),
            updated_at=datetime.fromisoformat(data["updatedAt"])
        )


def parse_arguments():
    """Parses command-line arguments and returns the command and its arguments."""
    if len(sys.argv) < 2:
        print("Usage: task_tracker.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    return command, args


def load_tasks():
    """Loads tasks from the JSON file or creates it if it doesn't exist."""
    tasks_file = "tasks.json"
    if not os.path.exists(tasks_file):
        with open(tasks_file, "w") as f:
            json.dump([], f)
        return []

    try:
        with open(tasks_file, "r") as f:
            tasks_data = json.load(f)
            return [Task.from_dict(task_data) for task_data in tasks_data]
    except json.JSONDecodeError:
        print(f"Error: Could not load tasks from {tasks_file}. File might be corrupted.")
        return []


def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    tasks_file = "tasks.json"
    with open(tasks_file, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4, default=str)


def _recalculate_ids(tasks):
    """Recalculates task IDs and sorts the task list."""
    for index, task in enumerate(tasks):
        task.id = index + 1
    tasks.sort(key=lambda task: task.id)


def add_task(tasks, description):
    """Adds a new task to the task list."""
    new_id = len(tasks) + 1
    new_task = Task(task_id=new_id, description=description)
    tasks.append(new_task)
    _recalculate_ids(tasks)
    print(f"Task added successfully (ID: {new_id})")


def update_task(tasks, task_id, description):
    """Updates the description of a task with the given ID."""
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return

    for task in tasks:
        if task.id == task_id:
            task.description = description
            task.updatedAt = datetime.now()
            print(f"Task with ID {task_id} updated successfully.")
            _recalculate_ids(tasks)
            return
    print(f"Error: Task with ID {task_id} not found.")


def delete_task(tasks, task_id):
    """Deletes a task with the given ID."""
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            print(f"Task with ID {task_id} deleted successfully.")
            _recalculate_ids(tasks)
            return
    print(f"Error: Task with ID {task_id} not found.")


def mark_task_progress(tasks, task_id):
    """Marks a task as in progress."""
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return

    for task in tasks:
        if task.id == task_id:
            task.mark_progress()
            print(f"Task with ID {task_id} marked as in progress.")
            _recalculate_ids(tasks)
            return
    print(f"Error: Task with ID {task_id} not found.")


def mark_task_done(tasks, task_id):
    """Marks a task as done."""
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return

    for task in tasks:
        if task.id == task_id:
            task.mark_done()
            print(f"Task with ID {task_id} marked as done.")
            _recalculate_ids(tasks)
            return
    print(f"Error: Task with ID {task_id} not found.")


def list_tasks(tasks, status=None):
    """Lists all tasks or tasks with a specific status."""
    if not tasks:
        print("No tasks found.")
        return

    if status:
        filtered_tasks = [task for task in tasks if task.status == status]
        if not filtered_tasks:
            print(f"No tasks found with status '{status}'.")
            return
        for task in filtered_tasks:
            print(
                f"ID: {task.id}, Description: {task.description}, Status: {task.status}, Created At: {task.createdAt}, Updated At: {task.updatedAt}")
    else:
        for task in tasks:
            print(
                f"ID: {task.id}, Description: {task.description}, Status: {task.status}, Created At: {task.createdAt}, Updated At: {task.updatedAt}")


if __name__ == "__main__":
    command, args = parse_arguments()
    tasks = load_tasks()

    if command == "add":
        if len(args) < 1:
            print("Usage: task_tracker.py add <description>")
        else:
            add_task(tasks, " ".join(args))
    elif command == "update":
        if len(args) < 2:
            print("Usage: task_tracker.py update <task_id> <description>")
        else:
            update_task(tasks, args[0], " ".join(args[1:]))
    elif command == "delete":
        if len(args) < 1:
            print("Usage: task_tracker.py delete <task_id>")
        else:
            delete_task(tasks, args[0])
    elif command == "mark-in-progress":
        if len(args) < 1:
            print("Usage: task_tracker.py mark-in-progress <task_id>")
        else:
            mark_task_progress(tasks, args[0])
    elif command == "mark-done":
        if len(args) < 1:
            print("Usage: task_tracker.py mark-done <task_id>")
        else:
            mark_task_done(tasks, args[0])
    elif command == "list":
        if len(args) == 0:
            list_tasks(tasks)
        elif len(args) == 1:
            list_tasks(tasks, args[0])
        else:
            print("Usage: task_tracker.py list [status]")
    else:
        print(f"Error: Unknown command '{command}'")

    save_tasks(tasks)
