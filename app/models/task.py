from enums.task_status_enum import TaskStatus
from models.user import User

class Task:
    def __init__(self, id = None, title = None, description = None, user = User(), status = TaskStatus.TODO):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__status = status
        self.__user = user
        
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value


    def to_short_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

    def to_dict(self):

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status.name,
            'user': self.user.name
        }