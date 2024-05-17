from rest_framework import serializers
from site_users.models import SiteUser

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
        print (user.exists())
        print (user.values('password'))
        print (user.values('password')[0]['password'])
        print (user.values_list('password', flat=True))
        print (user.values().first()['password'])
        if(1==1) :
            pass
        else :
            pass
        return data