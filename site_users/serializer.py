from rest_framework import serializers
from .models import SiteUser

from utils.datetime.datetimeutils import *

class SiteUsersSerializer(serializers.ModelSerializer):
    # last_modify = serializers.DateTimeField(source='modified_at') # Working 
    last_modify = serializers.SerializerMethodField('get_last_modify') 
    class Meta:
        model = SiteUser
        # exclude = ('id','password', 'created_at')
        # fields = '__all__'
        fields = ('user_name', 'first_name', 'middle_name', 'last_name', 'full_name', 'is_active', 'last_modify')

    def get_last_modify(self, obj):
        return DateTimeUtils().date_to_str(obj.modified_at, "%Y-%m-%d")