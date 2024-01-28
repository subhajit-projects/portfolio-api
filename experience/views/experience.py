from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, datetime
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

    def post(self, request):
        try:
            print(request.data)
            request_data = experienceSerializer(data=request.data)
            print (request_data.is_valid())
            print(request_data.data.get('designation', None))
            # request_data['']
            print (date.today())
            print(request_data.data.get('designation', None))
            print (datetime.strptime(request_data.data.get('work_end', None), "%Y-%m-%d")) #%d-%m-%Y"
            get_all_data = experience.objects.all()
            return_object = {
                "status": "success",
                "resp": "New experience added"
            }
            return Response(data=return_object, status=201)
        
        except ValueError:
            print("Error ")
        except Exception as e:
            print (e)