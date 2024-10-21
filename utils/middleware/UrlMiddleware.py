from django.conf import settings
from utils.exceptions.urlmiddlewareexception import UrlMiddlewareException
from django.http import HttpResponseServerError, JsonResponse
from utils.globalresponse import globalresponse
from utils.token.jwt import HS256JWT
from utils.exceptions.jwttokenexception import *

class UrlMiddleware(object):
    
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        # print ("init Middleware")
        self.get_response = get_response
    
    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later middleware) are called.
        """
        response = self.get_response(request)
        # print ("call Middleware")
        # print (request.META.get('HTTP_REFERER'))
        # print (request.META.get('HTTP_ACCEPT'))
        # print (request.META.get('HTTP_HOST'))
        # print (request.META.get('HTTP_USER_AGENT'))
        # print (request.META.get('REMOTE_ADDR'))
        # print (request.META.get('REMOTE_HOST'))
        # print (request.META.get('REQUEST_METHOD'))
        # print (request.META.get('SERVER_PORT'))
        # print (request.META.get('REMOTE_USER'))
        # print (request.META.get('QUERY_STRING'))

        try:
            if settings.DEBUG == False:
                if "Mozilla".lower() not in request.META.get('HTTP_USER_AGENT').lower() and request.META.get('HTTP_REFERER') == None :
                    # Check agent. Means the request came from postman or browser
                    raise UrlMiddlewareException("can't accept your request")
                    # response = HttpResponseServerError("Oops! Something went wrong.")

                if request.META.get('HTTP_AUTHORIZATION') == None or request.META.get('HTTP_AUTHORIZATION') == "" :
                    # Check bearer token is given or not
                    if str(request.get_full_path()).split("/")[-2] != "auth" or str(request.get_full_path()).split("/")[-2] != "get-token":
                        # check url is not for login
                        raise UrlMiddlewareException("token not provided")
                    
                if HS256JWT().get_header_data(request=request).get('type').upper() == "GET_ACCESS_ONLY" and request.META.get('REQUEST_METHOD').upper() != "GET":
                    raise UrlMiddlewareException("only get access only access for get request")
            

        except UrlMiddlewareException as e:
            data = {
                'message': str(e.message)
            }
            resp = globalresponse(error=data, status_code=406).response_data()
            response = JsonResponse(resp, safe=False, status=resp.get('status_code'))

        except JwtTokenException as e:
            data = {
                'message': str(e.message)
            }
            resp = globalresponse(error=data, status_code=406).response_data()
            response = JsonResponse(resp, safe=False, status=resp.get('status_code'))

        except Exception as e:
            response = HttpResponseServerError(e.message)       
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Called just before Django calls the view.
        """
        return None

    def process_exception(self, request, exception):
        """
        Called when a view raises an exception.
        """
        return None

    def process_template_response(self, request, response):
        """
        Called just after the view has finished executing.
        """
        return response