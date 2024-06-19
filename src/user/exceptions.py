class UserIdAlreadyExistsException(Exception):
    def __init__(self, id: str):
        self.id = id

class UserEmailAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email
        
class InvalidCredentialsException(Exception):
    def __init__(self, detail: str = "Invalid credentials"):
        self.detail = detail

class OperationNotPermittedException(Exception):
    def __init__(self, detail: str = "Operation not permitted"):
        self.detail = detail
