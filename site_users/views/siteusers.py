from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import *
from .. serializer import *
from utils.encrypt.pbkdf2sha256 import pbkdf2sha256

class siteusers(APIView):
    def get(self, request):
        # try:
            print ("*********************************************")
            get_all_data = SiteUser.objects.all()
            for a in get_all_data:
                print (a.password, pbkdf2sha256().verify("abcd", a.password))
            return_object = {
                "status": "success",
                "data": SiteUsersSerializer(get_all_data, many=True).data
            }
            return Response(data=return_object, status=200)
        # except Exception as e:
            # print (e)