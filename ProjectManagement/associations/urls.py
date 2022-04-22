from django.urls import path
from . import views

urlpatterns = [
    path('All', views.All, name='All'),
    path("profile/<str:pk>/", views.profile, name="profile"),  
]