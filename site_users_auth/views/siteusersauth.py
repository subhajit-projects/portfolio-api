# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.globalresponse import globalresponse

# Create your views here.

class SiteUsersAuth(APIView):
    def get(self, request):
        # return_object = {
        #     "status": "success",
        #     "data": SiteUsersSerializer(get_all_data, many=True).data
        # }
        
        return_obj = globalresponse(data=[], is_success=True, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))