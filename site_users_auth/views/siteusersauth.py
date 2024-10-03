# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .. serializers.loginserializer import *
from site_users.models import SiteUser
from site_users.serializer import SiteUsersSerializer
from utils.globalresponse import globalresponse
from utils.token.jwt import HS256JWT
from utils.exceptions import RequiredfieldException
from django.utils import timezone
from utils.datetime.datetimeutils import DateTimeUtils
from django.conf import settings
import datetime

# Create your views here.

class SiteUsersAuth(APIView):

    allowed_methods = ['get', 'post']

    def post(self, request):
        return_object = {
            # "status": "success",
            # "data": SiteUsersSerializer(get_all_data, many=True).data
        }

        request_data =request.data
        check_request_data = LoginFormSerializer(data=request_data)

        if check_request_data.is_valid(raise_exception=False):
            login_user_data = SiteUser.objects.filter(user_name=request_data.get('user_name')).first() 
            print (login_user_data.id)
            user = SiteUsersSerializer(login_user_data , many=False).data
            return_object['user'] = user
            # print (HS256JWT().decode("eyJhbGciOiJIUzI1NiIsImlkIjoiZGphbmdvLW15LXBvcnRmb2xpbyIsInR5cCI6IkpXVCIsInR5cGUiOiJBQ0NFU1MifQ.eyJkYXRhIjp7ImlkIjoiNzFiYTY0ZjktNTc0Ny00ZTAxLThhYTUtZGE0YzUyZmMwNWIxIiwiZW1haWwiOiJhYSAxMTExMSIsImV4cCI6IjE3MTYyNTUwMzQifX0.aEYTcVkrR_KImWSsOp1XBbUbrjxon__ejDMjFOlWtCo"))
            token = {}
            token['access_token'] = HS256JWT().encode({'id': str(login_user_data.id), 'email': login_user_data.full_name}, type="access")
            token['refresh_token'] = HS256JWT().encode({'id': str(login_user_data.id), 'email': login_user_data.full_name}, type="refresh")
            expire_time = datetime.datetime.now(tz=timezone.get_default_timezone()) + datetime.timedelta(seconds=settings.ACCESS_TOKEN_TIME)
            token['expire'] = DateTimeUtils().date_to_str(expire_time, "%Y-%m-%d %H:%M:%S")         
            return_object['token'] = token
            
        else:
            default_errors = check_request_data.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                # print ('field_errors: '+str(field_errors))
                field_names.append(field_name)
                raise RequiredfieldException(str(field_errors[0]), field_name)
        
        return_obj = globalresponse(data=return_object, is_success=True, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))