import json
import logging
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .tasks import StatusEnum, Task

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

PATH = Path.joinpath(Path(__file__).parent.parent.parent, "tasks.json")


@dataclass
class Taskboard():
    tasks: dict[str, Task] = field(default_factory=dict)

    def __post_init__(self):
        try:
            with open(PATH, "r") as file:
                data = json.load(file)
                for id, task in data.items():
                    t = Task()
                    t.from_dict(task)
                    self.tasks[id] = t
        except FileNotFoundError:
            with open(PATH, "w") as file:
                json.dump({}, file)

    def update_tasks(self):
        to_save = {task_id: asdict(task)
                   for task_id, task in self.tasks.items()}
        with open(PATH, "w") as file:
            json.dump(to_save, file, indent=4)

    def add_task(self, *task_args):
        if len(task_args) == 1:
            task = Task(name=task_args[0])
        else:
            task = Task(name=task_args[0], notes=task_args[1])
        self.tasks[task.id] = task
        self.update_tasks()
        logging.info(f"New task created! TaskID: {task.id}")
        return task

    def add_notes(self, task_id, task_notes):
        try:
            self.tasks[task_id].notes = task_notes
            self.update_tasks()
        except KeyError:
            logging.error(f"Task with ID '{task_id}' not found")

    def add_subtask(self, parent_task_id, *subtask_args):
        try:
            if len(subtask_args) == 1:
                task = Task(name=subtask_args[0])
            else:
                task = Task(name=subtask_args[0], notes=subtask_args[1])
            self.tasks[parent_task_id].add_subtask(task)
            self.update_tasks()
        except KeyError:
            logging.error(f"Task with ID '{parent_task_id}' not found")

    def delete_task(self, task_id):
        try:
            self.tasks.pop(task_id)
            self.update_tasks()
        except KeyError:
            logging.error(f"Task with ID {task_id} not in todo list")

    def list_tasks(self):
        print("  ID     NAME    STATUS")
        for count, id in enumerate(self.tasks):
            print(
                f'{count+1} {id} \
                {self.tasks[id].name} {self.tasks[id].status}'
            )

    def display_task(self, task_id):
        t = self.tasks[task_id]
        for key, value in asdict(t).items():
            print(key.upper(), value)

    def filter_list(self, status):
        print(" ID    NAME    STATUS")
        for count, id in enumerate(self.tasks):
            if self.tasks[id].status == status:
                print(f'{id} {self.tasks[id].name} {self.tasks[id].status}')

    def update_status(self, task_id, status):
        if task_id not in self.tasks.keys():
            logging.error(f"Task with ID {task_id} not found")
            return None
        try:
            self.tasks[task_id].status = StatusEnum[status].value
            self.update_tasks()
        except KeyError:
            logging.error(
                f"Invalid Coise: '{status}'\
                (choose from \
                {[status for status in StatusEnum.__members__.keys()]}"
            )
