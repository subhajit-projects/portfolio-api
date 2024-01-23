from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import *
from .. serializer import *
from django.conf import settings

class blog_details(APIView):
    def get(self, request, post_id):
        try:
            get_all_data = Blog.objects.filter(blog_id=post_id)
            return_object = {
                "status": "success",
                "data": singleBlogDetails(get_all_data, many=True).data
            }
            for i in range(0, len(return_object["data"])):
                if return_object["data"][i]["blog_image"] != '' and return_object["data"][i]["blog_image"] != None:
                    return_object["data"][i]["blog_image"] = settings.MEDIA_BASE_URL+return_object["data"][i]["blog_image"]
            return Response(data=return_object, status=200)
        except Exception as e:
            print (e)