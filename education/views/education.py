from rest_framework.views import APIView
from rest_framework.response import Response
from utils.globalresponse import globalresponse
from .. models import *
from .. serializer import *

class education_api(APIView):
    def get(self, request, education_id=""):
        try:
            many_data = True
            if education_id == "" :
                get_all_data = education.objects.all()
            else :
                get_all_data = education.objects.filter(education_id=education_id)
                if get_all_data.exists() == False:
                    raise ValueError("Education id not found")
                else:
                    get_all_data = get_all_data.first()
                    many_data = False
            # print(get_all_data.count())
            return_object = {
                "status": "success",
                "data": educationSerializer(get_all_data, many=many_data).data
            }
            return Response(data=return_object, status=200)
        except ValueError as e:
            raise ValueError(e)
        except Exception as e:
            print (e)
    
    def post(self, request):
        request_data = educationSerializer(data=request.data)
        return_object = {}

        if request_data.is_valid(raise_exception=False):
            request_data.save()
            data = {
                "message": "new edcation added"
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
    
    def put(self, request, education_id=""):
        try:
            request_data = educationSerializer(data=request.data)
            if education_id == None or education_id == "" :
                raise RequiredfieldException("education id required", "education_id")
            else :
                get_all_data = education.objects.filter(education_id=education_id)
                if get_all_data.exists() == False:
                    raise ValueError("education id not found")
                else:
                    if request_data.is_valid(raise_exception=False):
                        get_all_data.update(
                            streem = request_data.data['streem'],
                            institute_name = request_data.data['institute_name'],
                            start_year = request_data.data['start_year'],
                            end_year = request_data.data['end_year'],
                            is_continue = request_data.data['is_continue']
                        )
                    else:
                        default_errors = request_data.errors
                        field_names = []
                        for field_name, field_errors in default_errors.items():
                            field_names.append(field_name)
                            raise RequiredfieldException(str(field_errors[0]), field_name)
                #ValidationError
            data = {
                "message": "education updated"
            }
            return_object = globalresponse(data=data, is_success=True, status_code=201).response_data()

            return Response(data=return_object, status=return_object.get("status_code"))
                
        except RequiredfieldException as e:
            raise RequiredfieldException(e.message, e.field_name)
        
        except ValueError as e:
            raise ValueError(e)

        except Exception as e:
            print (e)
            raise Exception(e)