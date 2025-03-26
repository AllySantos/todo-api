
class User:
    def __init__(self, id = None, name = None, email = None, password = None):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password

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

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        return f'{self.id} | Name: {self.name} E-mail: {self.email}'

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email
        }
