class FieldvalueException(Exception):

    def __init__(self, message, field_name):
        super().__init__(message)

        self.message = message
        self.field_name = field_name