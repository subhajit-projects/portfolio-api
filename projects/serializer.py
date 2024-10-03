from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import project

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        exclude = ('id',)

        extra_kwargs = {
                "project_name": {"error_messages": {"required": "project name required"}},
                "project_sort_desc": {"error_messages": {"required": "project sort desc required"}},
                "project_desc": {"error_messages": {"required": "project desc required"}},
                # project_link
                "project_downlod_able": {"error_messages": {"required": "project dowloadable required"}},
                # project_image
                # project_file
            }
        
        # def update(self, instance, validated_data):
        #     instance.project_name = validated_data.get('project_name', instance.project_name)
        #     instance.project_sort_desc = validated_data.get('project_name', instance.project_sort_desc)
        #     instance.project_desc = validated_data.get('project_name', instance.project_desc)
        #     instance.project_link = validated_data.get('project_name', instance.project_link)
        #     instance.project_downlod_able = validated_data.get('project_name', instance.project_downlod_able)
        #     instance.project_image = validated_data.get('project_name', instance.project_image)
        #     instance.project_file = validated_data.get('project_name', instance.project_file)
        #     instance.save()
        #     return instance