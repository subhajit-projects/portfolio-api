from django.utils import timezone
from utils.exceptions.jwttokenexception import *
from django.conf import settings
import jwt
import datetime
import time
import pytz

class HS256JWT:
    __access_header = {'id': 'django-my-portfolio', 'type': 'ACCESS'}
    __refresh_header = {'id': 'django-my-portfolio', 'type': 'REFRESH'}
    __secret_key = settings.JWT_SECRET_KEY

    def encode(self, payload={}, algorithm="hs256", type ='access'):
        # token = jwt.encode(payload, "aa", algorithm.upper())
        # payload['exp'] = str(datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=30))        
        # print (datetime.datetime.now(tz=timezone.get_default_timezone()).timestamp())
        # print (datetime.timedelta(seconds=30))
        # print (datetime.datetime.now().time())
        # print (time.time())
        # print (datetime.datetime.now(tz=timezone.get_default_timezone()) + datetime.timedelta(seconds=30))
        # payload['exp'] = str(int(round(datetime.datetime.now(tz=timezone.get_default_timezone()).timestamp())))
        # print (payload)
        if type.upper() == "ACCESS":
            # timezone.utc
            expire_time = datetime.datetime.now(tz=pytz.timezone('Utc')) + datetime.timedelta(seconds=settings.ACCESS_TOKEN_TIME) # 60*10
            payload['exp'] = str(int(round(expire_time.timestamp())))
            token = jwt.encode({"data": payload}, self.__secret_key, algorithm=algorithm.upper(), headers=self.__access_header)

        if type.upper() == "REFRESH":
            # timezone.utc
            expire_time = datetime.datetime.now(tz=pytz.timezone('Utc')) + datetime.timedelta(seconds=settings.REFRESH_TOKEN_TIME) # 60*10
            payload['exp'] = str(int(round(expire_time.timestamp())))
            token = jwt.encode({"data": payload}, self.__secret_key, algorithm=algorithm.upper(), headers=self.__refresh_header)

        return token
    
    def decode(self, encode_key,  algorithm="hs256"):
        data = jwt.decode(encode_key, self.__secret_key, leeway=0, algorithms=algorithm.upper())
        header = jwt.get_unverified_header(encode_key)
        self.verify(data, header)
        print (header)
        return data
    
    def verify(self, token_data, token_header):
        # print (time.time())
        current_date_time = datetime.datetime.now(tz=timezone.utc)
        current_timestamp = int(round(current_date_time.timestamp()))
        msg = "Token Expire."
        if str(token_header.get('type')).upper() == "REFRESH":
            msg = "Refresh Token Expire."
        if str(token_header.get('type')).upper() == "ACCESS":
            msg = "Access Token Expire."
        if token_data.get('data').get('exp') < str(current_timestamp) :
            raise JwtTokenException(msg)