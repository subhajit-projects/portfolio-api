from rest_framework.views import APIView
from rest_framework.response import Response
from utils.token.jwt import HS256JWT
from utils.globalresponse import globalresponse

class ViewerToken(APIView):

    def post(self, request):
        # This request generate a token for only GET access
        print (request.get_full_path())
        print (request.META.get('HTTP_REFERER'))
        return_object = {}
        token = {}
        token['access_token'] = HS256JWT().encode({'id': 'user_id', 'email': 'user_email_id'}, type="GET_ACCESS_ONLY")
        return_object['token'] = token
        return_obj = globalresponse(data=return_object, is_success=True, status_code=200).response_data()
        return Response(data=return_obj, status=return_obj.get("status_code"))