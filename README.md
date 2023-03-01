# Todo List Python CLI

Todo list command-line application where we can organize our list of tasks through a bash command line, and we do not need to run any script or program explicitly.

## Setup

1. Create a virtual environment

    ```terminal
    python -m venv .venv
    ```

2. Activate virtual environment

    ```terminal
    source .venv/bin/activate
    ```

3. Install dependencies

    ```terminal
    pip intall -r requirements.txt    
    ```
## Usage

To run the script in the command line, use the following syntax:

    
    python todo_list.py <command> [args]
    
    
where `<command>` is one of the following options:

- `-h`, `--help`: Show help message with command options.
- `-v`, `--version`: Show program's version number.
- `-a [task_name]`, `--add [task_name]`: Add a new task on the list.
- `-ls`, `--list_tasks`: Display the list of tasks.
- `-d [task_id]`, `--delete [taskid]`: Delete task from the list
- `-s [task_id][subtask_name][subtask_notes]`: Add a subtask in an existing task in the list. Subtask_notes are optional.
- `-n [task_id]`, `--notes [task_id]`: Add notes to an existing task in the list
- `-ds [task_id]`, `--display_task [task_id]`: Provide task ID to display that task
- `-st [task_id][status]`, `--status[task_id][status]`: Update the status of a task. Choose from ('NOT_STARTED', 'IN_PROGRESS', 'COMPLETED')
- `-f [status]`, `--filter_list [status]`: Display the list of tasks filtered by the given status.