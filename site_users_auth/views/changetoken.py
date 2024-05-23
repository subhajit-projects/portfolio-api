from rest_framework.views import APIView
from rest_framework.response import Response
from utils.globalresponse import globalresponse
from utils.token.jwt import HS256JWT
from utils.datetime.datetimeutils import DateTimeUtils
from utils.exceptions.jwttokenexception import JwtTokenException
from django.utils import timezone
from django.conf import settings
import datetime

class ChangeToken(APIView):

    def post(self, request):
        return_object = {}
        request_data =request.data

        print (request_data.get('refresh-token'))
        if(request_data.get('refresh-token') == None or request_data.get('refresh-token') == ""):
            raise JwtTokenException("Refresh token required.")
        
        token_body = HS256JWT().decode(encode_key=request_data.get('refresh-token'))
        token = {}
        token['access_token'] = HS256JWT().encode({'id': token_body.get('data').get('id'), 'email': token_body.get('data').get('email')}, type="access")
        expire_time = datetime.datetime.now(tz=timezone.get_default_timezone()) + datetime.timedelta(seconds=settings.ACCESS_TOKEN_TIME)
        token['expire'] = DateTimeUtils().date_to_str(expire_time, "%Y-%m-%d %H:%M:%S")         
        return_object['token'] = token
        return_obj = globalresponse(data=return_object, is_success=True, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))