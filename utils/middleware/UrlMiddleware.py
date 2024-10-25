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
        print ("***************** call Middleware ***********************")
        print ('HTTP_REFERER: '+ str(request.META.get('HTTP_REFERER')))
        print ('HTTP_ACCEPT: '+ str(request.META.get('HTTP_ACCEPT')))
        print ('HTTP_HOST: '+ str(request.META.get('HTTP_HOST')))
        print ('HTTP_USER_AGENT: '+ str(request.META.get('HTTP_USER_AGENT')))
        print ('REMOTE_ADDR: '+ str(request.META.get('REMOTE_ADDR')))
        print ('REMOTE_HOST: '+ str(request.META.get('REMOTE_HOST')))
        print ('REQUEST_METHOD: '+ str(request.META.get('REQUEST_METHOD')))
        print ('SERVER_PORT: '+ str(request.META.get('SERVER_PORT')))
        print ('REMOTE_USER: '+ str(request.META.get('REMOTE_USER')))
        print ('QUERY_STRING: '+ str(request.META.get('QUERY_STRING')))
        print ('Content-Type: '+ str(request.META.get('Content-Type')))

        try:
            if settings.DEBUG == False:
                if "Mozilla".lower() not in request.META.get('HTTP_USER_AGENT').lower() and request.META.get('HTTP_REFERER') == None :
                    # Check agent. Means the request came from postman or browser
                    raise UrlMiddlewareException("can't accept your request")
                    # response = HttpResponseServerError("Oops! Something went wrong.")

                # Modify logic bellow
                # if request.META.get('HTTP_AUTHORIZATION') == None or request.META.get('HTTP_AUTHORIZATION') == "" :
                #     # Check bearer token is given or not
                #     print (request.get_full_path().split("/")[-2])
                #     if str(request.get_full_path()).split("/")[-2] != "auth" and str(request.get_full_path()).split("/")[-2] != "get-token" and "text/html" not in str(request.META.get('HTTP_ACCEPT')):
                #         # check url is not for login and not for generic access token and not from browser
                #         raise UrlMiddlewareException("token not provided")
                # else :
                #     if HS256JWT().get_header_data(request=request).get('type').upper() == "GET_ACCESS_ONLY" and request.META.get('REQUEST_METHOD').upper() != "GET":
                #         raise UrlMiddlewareException("only get access only access for get request")

                #First check is authorization is active
                if request.META.get('HTTP_AUTHORIZATION') != None and request.META.get('HTTP_AUTHORIZATION') != "" :
                    # Check request not came from auth, get-token or not accept type text/html
                    if str(request.get_full_path()).split("/")[-2] != "auth" and str(request.get_full_path()).split("/")[-2] != "get-token" and str(request.get_full_path()).split("/")[-2] != "refresh" and "text/html" not in str(request.META.get('HTTP_ACCEPT')):
                        # Check token type is GET_ACCESS_ONLY or ACCESS only
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
            print (e)
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