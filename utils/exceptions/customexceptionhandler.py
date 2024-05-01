from rest_framework.views import exception_handler
from django.http import JsonResponse
from rest_framework import status
from utils.globalresponse import globalresponse

def custom_exception_handler(exc, context):

    handlers = {
        'Exception': _handle_error_exception,
        'ValidationError': _handle_value_error_exception,
        'RequiredfieldException': _handle_required_field_error_exception,
        'PasswordException': _handle_password_error_exception,
        'MethodNotAllowed': _handle_method_not_allow_exception
    }

    response = exception_handler(exc, context)

    exception_class = exc.__class__.__name__

    print ("Exception class Name: "+str(exception_class))

    if exception_class in handlers:
        print (handlers.get(exception_class))
        # return handlers(exception_class)(exc, context, response)
        # print (handlers.get(exception_class)(exc, context, response))
        # print (response)
        err_data = {'MSG_HEADER': 'some custom error messaging'}
        # return JsonResponse(err_data, safe=False, status=503)
        resp = handlers.get(exception_class)(exc, context, response)
        return JsonResponse(resp, safe=False, status=resp.get('status_code'))
    else:
        return response

    # if response is not None:
    #     response.data['status_code'] = response.status_code

    # return response

def _handle_method_not_allow_exception(exc, context, response):
    response = response if response is not None else {}
    print (exc)
    print (context)
    data = {
        'message': "This method not allow."
    }
    response = globalresponse(error=data, status_code=405).response_data()
    return response

def _handle_error_exception(exc, context, response):
    response = response if response is not None else {}
    response['message'] = {
        'message': 'Error'
    }
    response['status'] = 503
    return response

def _handle_value_error_exception(exc, context, response):
    response = response if response is not None else {}
    response['message'] = {
        'message': str(exc)
    }
    response['status'] = 503
    # print (exc['designation'])
    return response

def _handle_required_field_error_exception(exc, context, response):
    response = response if response is not None else {}
    # response['message'] = {
    #     'message': str(exc.message),
    #     'field_name': exc.field_name
    # }
    # response['status'] = status.HTTP_400_BAD_REQUEST
    data = {
        'message': str(exc.message),
        'field_name': exc.field_name
    }
    response = globalresponse(error=data, status_code=400).response_data()
    return response

def _handle_password_error_exception(exc, context, response):
    response = response if response is not None else {}
    # print (exc.raw_message)
    data = {
        'message': str(exc.message)
    }
    response = globalresponse(error=data, status_code=503).response_data()
    return response