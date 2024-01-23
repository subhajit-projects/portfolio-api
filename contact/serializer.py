from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import contact

class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        exclude = ('id',)