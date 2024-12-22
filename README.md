# Task Tracker CLI

A simple command-line task tracker to manage your tasks.

**Source of task:** [Task Tracker Project](https://roadmap.sh/projects/task-tracker)

## Installation

No installation is required. Simply download the `task_tracker.py` script.

## Usage

The task-cli is used with the following structure:

```bash
python task_tracker.py <command> [arguments]
```

### Available Commands:

•   **add <description>:** Adds a new task.
```bash
python task_tracker.py add "Buy groceries"
```

•   **update <task_id> <description>:** Updates the description of a task with the given ID.
```bash
python task_tracker.py update 1 "Buy groceries and cook dinner"
```

•   **delete <task_id>:** Deletes a task with the given ID.
```bash
python task_tracker.py delete 1
```

•   **mark-in-progress <task_id>:** Marks a task as in progress.
```bash
python task_tracker.py mark-in-progress 1
```

•   **mark-done <task_id>:** Marks a task as done.
```bash
python task_tracker.py mark-done 1
```

•   **list:** Lists all tasks.
```bash
python task_tracker.py list
```

•   **list <status>:** Lists tasks with a specific status (todo, in-progress, done).
```bash
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
```

## Examples

```bash
# Add a new task
python task_tracker.py add "Write a report"

# List all tasks
python task_tracker.py list

# Mark task 1 as in progress
python task_tracker.py mark-in-progress 1

# List tasks with status "in-progress"
python task_tracker.py list in-progress

# Mark task 1 as done
python task_tracker.py mark-done 1

# List all done tasks
python task_tracker.py list done

# Update the description of task with ID 1
python task_tracker.py update 1 "Write and submit the report"

# Delete task with ID 2
python task_tracker.py delete 2
```

## Contributing
If you have any suggestions or improvements, feel free to contribute to the project.

## License
This project is licensed under the MIT License.

