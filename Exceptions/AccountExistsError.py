class AccountExistsError(Exception):

    def __init__(self, message, error=None):
        super().__init__(message)
        self.error = error

    def __str__(self):
        return self.error
