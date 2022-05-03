from django.urls import path
from . import views



urlpatterns = [
    path('createPost', views.createPost, name='createPost'),
    path('showMyPosts/<str:pk>/', views.showMyPosts, name='showMyPosts'),
    path('editPost/<str:pk>/', views.editPost, name='editPost'),


]