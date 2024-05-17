# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .. serializers.loginserializer import *
from utils.globalresponse import globalresponse
from utils.exceptions import RequiredfieldException

# Create your views here.

class SiteUsersAuth(APIView):
    def post(self, request):
        # return_object = {
        #     "status": "success",
        #     "data": SiteUsersSerializer(get_all_data, many=True).data
        # }

        request_data = LoginFormSerializer(data=request.data)
        if request_data.is_valid(raise_exception=False):
            pass
        else:
            default_errors = request_data.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                # print ('field_errors: '+str(field_errors))
                field_names.append(field_name)
                raise RequiredfieldException(str(field_errors[0]), field_name)
        
        return_obj = globalresponse(data=[], is_success=True, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))