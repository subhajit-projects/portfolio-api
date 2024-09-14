from django.db import models
from django.db.models import fields
from rest_framework import serializers
from utils.exceptions.requiredfieldexception import RequiredfieldException
from .models import About

class aboutSerializer(serializers.ModelSerializer):
    # start_date = serializers.SerializerMethodField('get_work_start') # To change field name

    class Meta:
        model = About
        exclude = ('id', 'created_at', 'modified_at')
        # fields = '__all__'
        extra_kwargs = {
                "about_content": {"error_messages": {"required": "content required"}},
                "is_active": {"error_messages": {"invalid": "invalid boolean format"}},
            }

    # def get_work_start(self, obj): # To change field name
        # return obj.work_start