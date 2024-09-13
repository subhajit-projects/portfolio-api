from django.db import models
from django.db.models import fields
from rest_framework import serializers
from utils.exceptions.requiredfieldexception import RequiredfieldException
from .models import Skill

class skillSerializer(serializers.ModelSerializer):
    # start_date = serializers.SerializerMethodField('get_work_start') # To change field name

    class Meta:
        model = Skill
        exclude = ('id', 'created_at', 'modified_at')
        # fields = '__all__'
        extra_kwargs = {
                "skill_name": {"error_messages": {"required": "skill name required"}},
                "skill_icon_name": {"error_messages": {"required": "skill icon name required"}},
                "skill_rating": {"error_messages": {"required": "skill rating required", 'blank': "work start sould not blank", "invalid": "invalid number format."}},
                "skill_sequance": {"error_messages": {"required": "skill sequance required", "invalid": "invalid number format"}},
                "is_active": {"error_messages": {"required": "skill active required", "invalid": "invalid boolean format"}},
            }

    # def get_work_start(self, obj): # To change field name
        # return obj.work_start