from rest_framework.views import APIView
from rest_framework.response import Response
from utils.globalresponse import globalresponse
from .. models import *
from .. serializer import *
from django.conf import settings
from utils.exceptions.requiredfieldexception import RequiredfieldException

class project_api(APIView):
    def get(self, request, project_id=""):
        '''
        try:
            get_all_data = project.objects.all()
            return_object = {
                "status": "success",
                "data": projectSerializer(get_all_data, many=True).data
            }

            for i in range(0, len(return_object["data"])):
                return_object["data"][i]["project_image"] = settings.MEDIA_BASE_URL+return_object["data"][i]["project_image"]

            for i in range(0, len(return_object["data"])):
                if return_object["data"][i]["project_file"] != "" and return_object["data"][i]["project_file"] != None:
                    return_object["data"][i]["project_file"] = settings.MEDIA_BASE_URL+return_object["data"][i]["project_file"]

            return Response(data=return_object, status=200)
        except Exception as e:
            print (e)
        '''
        try:
            many_data = True
            if project_id == "" :
                get_all_data = project.objects.all()
            else :
                get_all_data = project.objects.filter(project_id=project_id)
                if get_all_data.exists() == False:
                    raise ValueError("Project id not found")
                else:
                    get_all_data = get_all_data.first()
                    many_data = False
            return_object = {
                "status": "success",
                "data": projectSerializer(get_all_data, many=many_data).data
            }
            return Response(data=return_object, status=200)
        except ValueError as e:
            raise ValueError(e)
        except Exception as e:
            print (e)

    def post(self, request):
        request_data = projectSerializer(data=request.data)
        return_object = {}

        if request_data.is_valid(raise_exception=False):
            request_data.save()
            data = {
                "message": "new project added"
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
    
    def put(self, request, project_id=""):
        try:
            # request_data = projectSerializer(data=request.data, partial=True)
            if project_id == None or project_id == "" :
                raise RequiredfieldException("project id required", "education_id")
            else :
                get_all_data = project.objects.filter(project_id=project_id)
                if get_all_data.exists() == False:
                    raise ValueError("project id not found")
                else:
                    request_data = projectSerializer(data=request.data, partial=True)
                    if request_data.is_valid(raise_exception=False):
                        # print (request_data.data.get('project_name'))
                        # request_data.update(get_all_data, request.data)
                        # request_data['id'] = get_all_data.get().id
                        # request_data.update(get_all_data.get(), request.data)
                        # get_all_data.update(
                        #     project_name = request_data.data['project_name'],
                        #     project_sort_desc = request_data.data['project_sort_desc'],
                        #     project_desc = request_data.data['project_desc'],
                        #     project_link = request_data.data['project_link'],
                        #     project_downlod_able = request_data.data['project_downlod_able']
                        # )
                        # print (request_data.FILES['project_image'])
                        # if request.data['project_image'] != None and request.data['project_image'] != "":
                        #     get_all_data.update(
                        #     project_image = request.data['project_image']
                        # )
                        # if request.data['project_file'] != None:
                        #     get_all_data.update(
                        #     project_file = request.data['project_file']
                        # )
                        # get_all_data.project_name = request_data.data['project_name'],
                        # get_all_data.project_sort_desc = request_data.data['project_sort_desc'],
                        # get_all_data.project_desc = request_data.data['project_desc'],
                        # get_all_data.project_link = request_data.data['project_link'],
                        # get_all_data.project_downlod_able = request_data.data['project_downlod_able']
                        # print (request.FILES.get('project_image'))
                        # if request.data.get('project_image') == None or request.data.get('project_image') == "":
                        #     print ("update1111")
                        #     get_all_data.project_image = request.FILES.get('project_image')
                        #     # request.data['project_image'] = get_all_data.get().project_image
                        #     get_all_data.get().project_image = ""
                        # # if request.data['project_file'] != None and request.data['project_image'] != "":
                        # #     get_all_data.project_file = request.data['project_file']
                        # # get_all_data.update()
                        # get_all_data.save()
                        # print (request.data)
                        # request_data.update(get_all_data.get(), request.data, partial=True)

                        get_all_data = get_all_data.get()
                        get_all_data.project_name = request.data.get('project_name', get_all_data.project_name)
                        get_all_data.project_sort_desc = request.data.get('project_sort_desc', get_all_data.project_sort_desc)
                        get_all_data.project_desc = request.data.get('project_desc', get_all_data.project_desc)
                        get_all_data.project_link = request.data.get('project_link', get_all_data.project_link)
                        get_all_data.project_downlod_able = request.data.get('project_downlod_able', get_all_data.project_downlod_able)
                        if request.FILES.get('project_image') != None and request.data.get('project_image') != "":
                            get_all_data.project_image = request.FILES.get('project_image', get_all_data.project_image)
                        if request.FILES.get('project_file') != None and request.data.get('project_file') != "":
                            get_all_data.project_file = request.FILES.get('project_file', get_all_data.project_image)
                        get_all_data.save()
                        print (request.FILES.get('project_image'))
                        print (request.data.get('project_image'))

                    else:
                        default_errors = request_data.errors
                        field_names = []
                        for field_name, field_errors in default_errors.items():
                            field_names.append(field_name)
                            raise RequiredfieldException(str(field_errors[0]), field_name)
                #ValidationError
            data = {
                "message": "project updated"
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