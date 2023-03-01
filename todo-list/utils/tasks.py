import random
import string
from dataclasses import dataclass, field
from enum import Enum


class StatusEnum(Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


@dataclass
class Task:
    name: str = field(default="")
    notes: str = field(default="")
    status: str = field(default=StatusEnum.NOT_STARTED.value)
    subtasks: list = field(default_factory=list)
    id: int = field(init=False,
                    default_factory=lambda:
                    "".join(random.choices(string.digits, k=4)))

    def from_dict(self, tasks_dict):
        self.name = tasks_dict["name"]
        self.notes = tasks_dict["notes"]
        self.status = tasks_dict["status"]
        self.subtasks = tasks_dict["subtasks"]
        self.id = tasks_dict["id"]

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)
