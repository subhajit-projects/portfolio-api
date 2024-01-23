from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Blog

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ('id', 'blog_content', )

class singleBlogDetails(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ('id', 'blog_sort_desc', 'blog_sl_no', )