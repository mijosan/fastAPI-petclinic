class UserIdAlreadyExistsException(Exception):
    def __init__(self, id: str):
        self.id = id

class UserEmailAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email