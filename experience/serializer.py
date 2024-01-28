from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import experience

class experienceSerializer(serializers.ModelSerializer):
    # start_date = serializers.SerializerMethodField('get_work_start') # To change field name

    class Meta:
        model = experience
        # fields = ('designation','company_name','work_start','work_end','is_continue','what_to_do','start_date')
        exclude = ('id',)

    # def get_work_start(self, obj): # To change field name
        # return obj.work_start

    def validate(self, data):
        if data['company_name'] == None:
            raise serializers.ValidationError('Rating has to be between 1 and 10.')
        return data