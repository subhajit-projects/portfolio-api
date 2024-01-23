from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import *
from .. serializer import *

class experience_api(APIView):
    def get(self, request):
        try:
            get_all_data = experience.objects.all()
            return_object = {
                "status": "success",
                "data": experienceSerializer(get_all_data, many=True).data
            }
            return Response(data=return_object, status=200)
        except Exception as e:
            print (e)