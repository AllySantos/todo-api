
class UserAlreadyExists(Exception):
    def __init__(self, message = "A user with this e-mail already exists"):
        self.message = message
        super().__init__(self.message)

class UserNotFound(Exception):
    def __init__(self, message = "User not found"):
        self.message = message
        super().__init__(self.message)

class TokenExpirated(Exception):
    def __init__(self, message = "Token has already expirated"):
        self.message = message
        super().__init__(self.message)

class UnauthorizedUser(Exception):
    def __init__(self, message="The user has not access to manage this task"):
        self.message = message
        super().__init__(self.message)

class TaskNotFound(Exception):
    def __init__(self, message = "Task not found"):
        self.message = message
        super().__init__(self.message)
