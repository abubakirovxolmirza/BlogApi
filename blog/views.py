from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from .serialazers import BlogSerializer
from django.contrib.auth.models import User


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@api_view(['GET'])
def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
        blogs = Blog.objects.filter(author=user)
        serializer = BlogSerializer(blogs, many=True)
        data = {
            'id': user.id,
            'author': user.username,
            'blogs': serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'message': f'User {username} not found.'}, status=status.HTTP_404_NOT_FOUND)
