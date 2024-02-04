from django.db import models
from django.db.models import fields
from rest_framework import serializers
from utils.exceptions.requiredfieldexception import RequiredfieldException
from .models import experience

class experienceSerializer(serializers.ModelSerializer):
    # start_date = serializers.SerializerMethodField('get_work_start') # To change field name

    class Meta:
        model = experience
        # fields = ('designation','company_name','work_start','work_end','is_continue','what_to_do','start_date')
        exclude = ('id',)
        extra_kwargs = {
                "designation": {"error_messages": {"required": "designation required"}},
                "company_name": {"error_messages": {"required": "company name required"}},
                "work_start": {"error_messages": {"required": "work start required", 'blank': "work start sould not blank", "invalid": "invalid date format. Please send YYYY-MM-DD"}},
                "work_end": {"error_messages": {"required": "work end required", "invalid": "invalid date format. Please send YYYY-MM-DD"}},
                "what_to_do": {"error_messages": {"required": "what to do required"}},
            }

    # def get_work_start(self, obj): # To change field name
        # return obj.work_start

    def validate(self, data):
        if data.get('work_start') >= data.get('work_end') :
            # raise serializers.ValidationError('start date mast be less then end date')
            raise RequiredfieldException('start date mast be less then end date', 'work_start')
        return data