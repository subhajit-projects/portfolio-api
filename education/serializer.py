from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import education

class educationSerializer(serializers.ModelSerializer):
    class Meta:
        model = education
        exclude = ('id',)