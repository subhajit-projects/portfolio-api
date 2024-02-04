class globalresponse:
    
    response = {
        "data": None,
        "error": None,
        "is_success": False,
        "status_code": 0

    }

    # def __init__(self):
    #     pass

    # def __init__(self, data):
    #     pass

    # def __init__(self, error, status_code):
    #     self.response["error"] = error
    #     self.response["status_code"] = status_code
    #     del(self.response['data'])

    def __init__(self, data={}, error={}, is_success=False, status_code=502):
        self.response["data"] = data
        self.response["error"] = error
        self.response["is_success"] = is_success
        self.response["status_code"] = status_code
        if len(data) == 0:
            del(self.response['data'])
        if len(error) == 0:
            del(self.response['error'])


    def response_data(self):
        return self.response