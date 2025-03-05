from enum import Enum

class TaskStatus(Enum):

    TODO = 0
    IN_PROGRESS = 1
    CANCELED = 2
    DONE = 3