
class User:
    def __init__(self, id = None, name = None, email = None):
        self.__id = id
        self.__name = name
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        return f'{self.id} | Name: {self.name} E-mail: {self.email}'