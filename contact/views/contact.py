from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import *
from .. serializer import *
from django.utils.datastructures import MultiValueDictKeyError

class contact_api(APIView):
    def get(self, request):
        try:
            get_all_data = contact.objects.all()
            print (get_all_data)
            return Response(data=contactSerializer(get_all_data, many=True).data, status=200)
        except Exception as e:
            print (e)
    
    def post(self, request):
        try:
            if 'first_name' not in request.data:
                raise MultiValueDictKeyError('first_name')

            if request.data['first_name'] == "":
                raise ValueError('first_name')
                
            if request.data['last_name'] == "":
                raise ValueError('last_name')
            
            if request.data['email_id'] == "":
                raise ValueError('email_id')

            if request.data['message'] == "":
                raise ValueError('message')

            store_contact = contact()
            store_contact.first_name = request.data['first_name']
            store_contact.last_name = request.data['last_name']
            store_contact.email_id = request.data['email_id']
            store_contact.message = request.data['message']
            store_contact.save()

            return_object = {
                "status": "success",
                "message": "Thnak you connect with me."
            }
            return Response(data=return_object, status=201)

        except MultiValueDictKeyError as e:
            # print ("**************Key error", e)
            return_object = {
                "status": "failed",
                "message": "Key not found: "+str(e)
            }
            return Response(data=return_object, status=400)

        except ValueError as e:
            # print ("*****************", e)
            return_object = {
                "status": "failed",
                "message": str(e)+ " required"
            }
            return Response(data=return_object, status=401)
        except Exception as e:
            # print (e.message())
            print (e)