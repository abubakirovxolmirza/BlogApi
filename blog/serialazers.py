# blog/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'created_at', 'author']
