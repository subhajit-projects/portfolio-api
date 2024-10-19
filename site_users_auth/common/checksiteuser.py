from site_users.models import SiteUser
from utils.token.jwt import HS256JWT

class CheckSiteUser:
    def getUserDetailsFromUserId(self, user_id=None):
        pass

    def getUserDetailsFromId(self, id=None):
        pass

    @classmethod
    def getUserDetailsFromToken(self, request=None):        
        get_user_id = SiteUser.objects.filter(id=HS256JWT().get_body_data(request=request).get('data').get('id'))
        return get_user_id.get()

    def getUserPermissionFromUserId(self, user_id=None):
        pass

    def getUserPermissionFromId(self, id=None):
        pass