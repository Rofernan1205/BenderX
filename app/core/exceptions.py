class BenderXError(Exception):
    def __init__(self, message="Ha ocurrido un error en el sistema"):
        self.message = message
        super().__init__(self.message)

class ValidationError(BenderXError):
    pass

class NotFoundError(BenderXError):
    pass

class UserNotFoundException(BenderXError):
    pass

class BranchNotFoundException(BenderXError):
    pass