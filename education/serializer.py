from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import education
from utils.exceptions.requiredfieldexception import RequiredfieldException

class educationSerializer(serializers.ModelSerializer):
    class Meta:
        model = education
        exclude = ('id',)
        extra_kwargs = {
                "streem": {"error_messages": {"required": "streem required"}},
                "institute_name": {"error_messages": {"required": "institute name required"}},
                "start_year": {"error_messages": {"required": "start year required", 'blank': "start year sould not blank", "invalid": "invalid date format. Please send YYYY", "invalid_choice": "invalid year format. Please send YYYY"}},
                "end_year": {"error_messages": {"required": "end year required", "invalid": "invalid date format. Please send YYYY", "invalid_choice": "invalid year format. Please send YYYY"}},
                "is_continue": {"error_messages": {"required": "is continue required"}},
            }
        
    def validate(self, data):
        if data.get('start_year') >= data.get('end_year') :
            # raise serializers.ValidationError('start date mast be less then end date')
            raise RequiredfieldException('start year mast be less then end year', 'start_year')
        return data