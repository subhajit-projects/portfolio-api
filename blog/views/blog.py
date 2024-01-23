from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import *
from .. serializer import *
from django.conf import settings

class blog_api(APIView):
    POST_SHOW_LIMIT = 6

    def get(self, request, page_no):
        try:
            data_fetch_limit = self.set_limit(page_no)
            total_page = self.count_total_page()
            get_all_data = Blog.objects.filter(blog_sl_no__range = data_fetch_limit)
            return_object = {
                "status": "success",
                "data": blogSerializer(get_all_data, many=True).data
            }

            for i in range(0, len(return_object["data"])):
                if return_object["data"][i]["blog_image"] != '' and return_object["data"][i]["blog_image"] != None:
                    return_object["data"][i]["blog_image"] = settings.MEDIA_BASE_URL+return_object["data"][i]["blog_image"]

            return_object['total_page_no'] = total_page
            return_object['current_page'] = page_no

            return Response(data=return_object, status=200)
        except Exception as e:
            print (e)

    def set_limit(self, page_no):
        range1 = page_no*self.POST_SHOW_LIMIT
        range2 = range1-self.POST_SHOW_LIMIT
        post_limit = [range2, range1-1]
        return post_limit

    def count_total_page(self):
        import math
        total_post_count = Blog.objects.count()
        total_page_count = total_post_count / self.POST_SHOW_LIMIT
        # total_page_count = 7 / self.POST_SHOW_LIMIT
        # print (total_page_count)
        # print (math.ceil(total_page_count))
        return math.ceil(total_page_count)