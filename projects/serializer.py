from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import project

class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        exclude = ('id',)