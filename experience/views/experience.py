from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, datetime

from utils.globalresponse import globalresponse
from .. models import *
from .. serializer import *
from rest_framework import serializers
from rest_framework import status
from utils.exceptions import RequiredfieldException

class experience_api(APIView):
    def get(self, request, experience_id=""):
        try:
            get_all_data = None
            many_data = True
            if experience_id == "" :
                get_all_data = experience.objects.all()
            else :
                get_all_data = experience.objects.filter(experience_id=experience_id)
                if get_all_data.exists() == False:
                    raise ValueError("Experience id not found")
                else:
                    get_all_data = get_all_data.first()
                    many_data = False
                #ValidationError
            return_object = {
                "status": "success",
                "data": experienceSerializer(get_all_data, many=many_data).data
            }
            return Response(data=return_object, status=200)
        except ValueError as e:
            raise ValueError(e)
        except Exception as e:
            print (e)
            raise Exception(e)

    def post(self, request):
        request_data = experienceSerializer(data=request.data)
        return_object = {}
        # print (request_data.is_valid())

        # if request_data.is_valid(raise_exception=True):
        if request_data.is_valid(raise_exception=False):
            # print (datetime.strptime(request_data.data.get('work_end', None), "%Y-%m-%d")) #%d-%m-%Y"
            # return_object = {
            #     "status": "success",
            #     "resp": "new experience added"
            # }
            # Save new Experience
            request_data.save()
            data = {
                "message": "new experience added"
            }
            return_object = globalresponse(data=data, is_success=True, status_code=201).response_data()
        else:
            default_errors = request_data.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                # print ('field_name: '+field_name)
                # print ('field_errors: '+str(field_errors))
                # print ('Single error: '+str(field_errors[0]))
                field_names.append(field_name)
                raise RequiredfieldException(str(field_errors[0]), field_name)

        return Response(data=return_object, status=return_object.get("status_code"))
    
    def put(self, request, experience_id=""):
        try:
            request_data = experienceSerializer(data=request.data)
            if experience_id == None or experience_id == "" :
                raise Exception("experience_id required")
            else :
                get_all_data = experience.objects.filter(experience_id=experience_id)
                if get_all_data.exists() == False:
                    raise Exception("Experience id not found")
                else:
                    if request_data.is_valid(raise_exception=False):
                        get_all_data.update(
                            designation = request_data.data['designation'],
                            company_name = request_data.data['company_name'],
                            work_start = request_data.data['work_start'],
                            work_end = request_data.data['work_end'],
                            is_continue = request_data.data['is_continue'],
                            what_to_do = request_data.data['what_to_do']
                        )
                    else:
                        default_errors = request_data.errors
                        field_names = []
                        for field_name, field_errors in default_errors.items():
                            field_names.append(field_name)
                            raise RequiredfieldException(str(field_errors[0]), field_name)
                #ValidationError
            data = {
                "message": "experience updated"
            }
            return_object = globalresponse(data=data, is_success=True, status_code=201).response_data()

            return Response(data=return_object, status=return_object.get("status_code"))
                
        except RequiredfieldException as e:
            raise RequiredfieldException(e.message, e.field_name)
        except Exception as e:
            print (e)
            raise Exception(e)