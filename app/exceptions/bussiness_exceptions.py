
class UserAlreadyExists(Exception):
    def __init__(self, message = "A user with this e-mail already exists"):
        self.message = message
        super().__init__(self.message)

class UserNotFound(Exception):
    def __init__(self, message = "User not found"):
        self.message = message
        super().__init__(self.message)
