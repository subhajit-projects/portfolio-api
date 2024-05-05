from datetime import datetime

class DateTimeUtils:
    def date_to_str(self, date=datetime.now(), format="%Y-%m-%d"):
        return date.strftime(format)