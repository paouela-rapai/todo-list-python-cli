from utils.loader import parse_args
from utils.taskboard import Taskboard

if __name__ == "__main__":
    args = parse_args()

    taskboard = Taskboard()

    if args.add:
        taskboard.add_task(*args.add)

    if args.notes:
        taskboard.add_notes(*args.notes)

    if args.subtask:
        taskboard.add_subtask(*args.subtask)

    if args.delete:
        taskboard.delete_task(args.delete)

    if args.list_tasks:
        taskboard.list_tasks()

    if args.display_task:
        taskboard.display_task(args.display_task)

    if args.status:
        taskboard.update_status(*args.status)

    if args.filter_list:
        taskboard.filter_list(args.filter)
