from rest_framework import serializers
from site_users.models import SiteUser
from utils.exceptions.loginexception import LoginException
from utils.encrypt.pbkdf2sha256 import Pbkdf2Sha256

class LoginFormSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(validators=[])
    user_name = serializers.CharField(error_messages={"required": "user name required", 'blank': "user name sould not blank"}) # required=True, allow_null=False
    class Meta:
        model = SiteUser
        fields = ('user_name', 'password')

        extra_kwargs = {
            "password": {"error_messages": {"required": "password required", 'blank': "password sould not blank"}},
        }
    
    def validate(self, data):
        user = SiteUser.objects.filter(user_name = data.get('user_name').lower())
        if user.exists() == False:
            raise LoginException("User not found.", 'user_name')
        # print (user.values('password'))
        # print (user.values('password')[0]['password'])
        # print (user.values_list('password', flat=True))
        # print (user.values().first()['password'])
        if Pbkdf2Sha256().verify(data.get('password'), user.values().first()['password']) == False:
            raise LoginException("Password not match.", 'password')
        if(1==1) :
            pass
        else :
            pass
        return data