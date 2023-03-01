import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Todo List",
        description="",
        usage="",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 1.0",
    )
    parser.add_argument(
        "-a",
        "--add",
        help="%(prog)s —add-task [task name]",
        type=str,
        nargs="*"
    )
    parser.add_argument(
        "-n",
        "--notes",
        help="add notes to task with taskID",
        type=str,
        nargs="*",
    )
    parser.add_argument(
        "-s",
        "--subtask",
        help="add [subtask_name] and [subtask_notes] to taskID",
        type=str,
        nargs="*"
    )
    parser.add_argument(
        "-d",
        "--delete",
        help="%(prog)s  —delete-task [task name]",
        type=str
    )
    parser.add_argument(
        "-ls",
        "--list_tasks",
        help="%(prog)s list tasks",
        action="store_true",
    )
    parser.add_argument(
        "-ds",
        "--display_task",
        help="provide taskID to display task",
        type=str,
    )
    parser.add_argument(
        "-st",
        "--status",
        help="update status of task",
        type=str,
        nargs=2
    )
    parser.add_argument(
        "-f",
        "--filter_list",
        help="filter list by status",
        type=str
    )

    return parser.parse_args()
