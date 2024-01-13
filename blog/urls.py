from django.urls import path
from .views import BlogList, BlogDetail, user_profile

urlpatterns = [
    path('new/', BlogList.as_view()),
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('user/<str:username>/', user_profile, name='user-profile'),
]
