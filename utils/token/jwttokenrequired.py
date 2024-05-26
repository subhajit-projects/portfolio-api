from utils.exceptions.jwttokenexception import JwtTokenException
from utils.token.jwt import HS256JWT

# def jwt_token_required(required=True):
#     # print ("this is 1")
#     def Inner(func):
#         # print ("this is 2")
#         def wrapper(request, *args, **kwargs):
#             print ("this is 3")
#             print (args)
#             print (kwargs)
#             print (request)
#             func(*args, **kwargs)

#         return wrapper
#     return Inner


# class  JWTTokenRequired:

#     def __init__(self, required=True):
#         self.required = required

#     def __call__(self, func):
#         def wrapper(self, request, *args, **kwargs):
#             print (args)
#             print (kwargs)
#             print (self.required)
#             print ()
#             print (request.data)
#             func(self, request, *args, **kwargs)

#         return wrapper


def JwtTokenRequired(required=True):
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            if 'HTTP_AUTHORIZATION' in request.META and request.META['HTTP_AUTHORIZATION'] != None and 'Bearer ' in request.META['HTTP_AUTHORIZATION']:
                raw_token = request.META['HTTP_AUTHORIZATION'].replace('Bearer ', '')
                token_body = HS256JWT().decode(encode_key=raw_token)
                # print (request.data)
                return func(self, request, *args, **kwargs)
            else :
                raise JwtTokenException('Token required.')
            # ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
            # if ip in WHITE_LIST:
            #     return func(request, *args, **kwargs)
            # else:
            #     return HttpResponseForbidden()
            
        return wrapper
    return decorator