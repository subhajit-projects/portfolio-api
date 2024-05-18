# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .. serializers.loginserializer import *
from site_users.models import SiteUser
from site_users.serializer import SiteUsersSerializer
from utils.globalresponse import globalresponse
from utils.exceptions import RequiredfieldException

# Create your views here.

class SiteUsersAuth(APIView):
    def post(self, request):
        return_object = {
            # "status": "success",
            # "data": SiteUsersSerializer(get_all_data, many=True).data
        }

        request_data = data=request.data
        check_request_data = LoginFormSerializer(data=request_data)

        if check_request_data.is_valid(raise_exception=False):
            token = {}
            token['access_token']=""
            token['expire']=""
            token['refresh_token']=""
            return_object['token'] = token
            user = SiteUsersSerializer(SiteUser.objects.filter(user_name=request_data.get('user_name')).first() , many=False).data
            return_object['user'] = user
        else:
            default_errors = check_request_data.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                # print ('field_errors: '+str(field_errors))
                field_names.append(field_name)
                raise RequiredfieldException(str(field_errors[0]), field_name)
        
        return_obj = globalresponse(data=return_object, is_success=True, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))