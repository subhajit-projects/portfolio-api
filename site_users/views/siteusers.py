from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import *
from .. serializer import *
from utils.encrypt.pbkdf2sha256 import pbkdf2sha256
from utils.globalresponse import globalresponse
from utils.exceptions import RequiredfieldException

class siteusers(APIView):
    def get(self, request):
        get_all_data = SiteUser.objects.all()
        # for a in get_all_data:
            # print (a.password, pbkdf2sha256().verify("abcd", a.password))
        return_object = {
            "status": "success",
            "data": SiteUsersSerializer(get_all_data, many=True).data
        }
        
        return_obj = globalresponse(data=SiteUsersSerializer(get_all_data, many=True).data, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))
    
    def post(self, request):
        resp_obj = {}
        request_data = SiteUsersSerializer(data=request.data)
        if request_data.is_valid(raise_exception=False):
            pass
        else:
            default_errors = request_data.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                field_names.append(field_name)
                raise RequiredfieldException(str(field_errors[0]), field_name)
        
        return_obj = globalresponse(data=SiteUsersSerializer(resp_obj).data, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))