from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import experience

class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = experience
        exclude = ('id',)