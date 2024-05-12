import re

class StringValidation:

    def name_validation(self, string):
        regx = re.compile(r'^[a-zA-z]*$', re.IGNORECASE)
        if regx.match(string):
            return True
        return False