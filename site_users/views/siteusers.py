from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import *
from .. serializer import *
from utils.globalresponse import globalresponse
from utils.exceptions import RequiredfieldException

class siteusers(APIView):
    def get(self, request, user_id=""):
        get_all_data = None
        many_data = True
        if user_id != "" :
            get_all_data = SiteUser.objects.filter(user_id=user_id)
            many_data = False
            if get_all_data.exists() == False:
                raise ValueError("user not found")
            get_all_data = get_all_data.first()
        else :
            get_all_data = SiteUser.objects.all()
        # for a in get_all_data:
            # print (a.password, pbkdf2sha256().verify("abcd", a.password))
        return_object = {
            "status": "success",
            "data": SiteUsersSerializer(get_all_data, many=many_data).data
        }
        
        # return_obj = globalresponse(data=SiteUsersSerializer(get_all_data, many=many_data).data, is_success=True, status_code=200).response_data()
        # return Response(data=return_obj, status=return_obj.get("status_code"))
        return Response(data=return_object, status=return_object.get("status_code"))
    
    def post(self, request):
        resp_obj = {}
        request_data = SiteUsersSerializerFormValidate(data=request.data)
        if request_data.is_valid(raise_exception=False):
            # print("Password")
            # print (request_data.get("user_name"))
            # request_data.save()
            request_data.create()
            # SiteUser().create(request_data)
            resp_obj = {
                "message": "new user added"
            }
            return_obj = globalresponse(data=resp_obj, is_success=True, status_code=201).response_data()
        else:
            default_errors = request_data.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                # print ('field_errors: '+str(field_errors))
                field_names.append(field_name)
                raise RequiredfieldException(str(field_errors[0]), field_name)
            
        return Response(data=return_obj, status=return_obj.get("status_code"))
    
    def put(self, request, user_id):
        resp_obj = {}
        request_data = SiteUsersSerializerFormValidateForEdit(data=request.data)
        if request_data.is_valid(raise_exception=False):
            get_data = SiteUser.objects.filter(user_id=user_id)
            if get_data.exists() == False:
                raise ValueError("user not found")
            
            get_data = get_data.get()
            get_data.first_name = request.data.get('first_name', get_data.first_name)
            get_data.middle_name = request.data.get('middle_name', get_data.middle_name)
            get_data.last_name = request.data.get('last_name', get_data.last_name)
            get_data.save()
            resp_obj = {
                "message": "user data uptodate"
            }
            return_obj = globalresponse(data=resp_obj, is_success=True, status_code=201).response_data()
        else:
            default_errors = request_data.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                # print ('field_errors: '+str(field_errors))
                field_names.append(field_name)
                raise RequiredfieldException(str(field_errors[0]), field_name)
            
        return Response(data=return_obj, status=return_obj.get("status_code"))
    
    def patch(self, request, user_id=None):
        data = request.data
        if data.get('password') == None:
            raise RequiredfieldException("password required", "password")
        get_data = SiteUser.objects.filter(user_id=user_id)
        if get_data.exists() == False:
            raise ValueError("user not found")
        get_data = get_data.get()
        get_data.password = get_data.password_encrypt(request.data.get('password'))
        get_data.save()
        resp_obj = {
                "message": "password update successfull"
            }
        return_obj = globalresponse(data=resp_obj, is_success=True, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))
