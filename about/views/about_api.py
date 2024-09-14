from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, datetime

from utils.globalresponse import globalresponse
from ..models import *
from .. serializer import *
from rest_framework import serializers
from rest_framework import status
from utils.exceptions import RequiredfieldException

class about_api(APIView):
    def get(self, request, about_id=""):
        try:
            get_all_data = None
            many_data = True
            if about_id == "" :
                get_all_data = About.objects.all()
                for a in get_all_data:
                    print ("Print ", a.about_content)
            else :
                get_all_data = About.objects.filter(about_id=about_id)
                if get_all_data.exists() == False:
                    raise ValueError("about id not found")
                else:
                    get_all_data = get_all_data.first()
                    many_data = False
                #ValidationError
            return_object = {
                "status": "success",
                "data": aboutSerializer(get_all_data, many=many_data).data
            }
            return Response(data=return_object, status=200)
        except ValueError as e:
            raise ValueError(e)
        except Exception as e:
            print (e)
            raise Exception(e)
        
    def post(self, request):
        request_data = aboutSerializer(data=request.data)
        return_object = {}
        # print (request_data.is_valid())

        # if request_data.is_valid(raise_exception=True):
        if request_data.is_valid(raise_exception=False):
            request_data.save()
            data = {
                "message": "new about added"
            }
            return_object = globalresponse(data=data, is_success=True, status_code=201).response_data()
        else:
            default_errors = request_data.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                field_names.append(field_name)
                raise RequiredfieldException(str(field_errors[0]), field_name)

        return Response(data=return_object, status=return_object.get("status_code"))
    
    def put(self, request, about_id=""):
        try:
            request_data = aboutSerializer(data=request.data)
            if about_id == None or about_id == "" :
                raise RequiredfieldException("about id required", "about_id")
            else :
                get_all_data = About.objects.filter(about_id=about_id)
                if get_all_data.exists() == False:
                    raise ValueError("about id not found")
                else:
                    if request_data.is_valid(raise_exception=False):
                        get_all_data.update(
                            about_content = request_data.data['about_content'],
                            is_active = request_data.data['is_active']
                        )
                    else:
                        default_errors = request_data.errors
                        field_names = []
                        for field_name, field_errors in default_errors.items():
                            field_names.append(field_name)
                            raise RequiredfieldException(str(field_errors[0]), field_name)
                #ValidationError
            data = {
                "message": "about updated"
            }
            return_object = globalresponse(data=data, is_success=True, status_code=200).response_data()

            return Response(data=return_object, status=return_object.get("status_code"))
                
        except RequiredfieldException as e:
            raise RequiredfieldException(e.message, e.field_name)
        
        except ValueError as e:
            raise ValueError(e)

        except Exception as e:
            print (e)
            raise Exception(e)