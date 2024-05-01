class PasswordException(Exception):

    def __init__(self, message, raw_message):
        super().__init__(message)

        self.message = message
        self.raw_message = raw_message
