class AccountNotExistsError(Exception):

    def __init__(self, error=None, message=None):
        super().__init__(message)
        self.error = error

    def __str__(self):
        return self.error
