from rest_framework import serializers
from .models import SiteUser

class SiteUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        exclude = ('id',)