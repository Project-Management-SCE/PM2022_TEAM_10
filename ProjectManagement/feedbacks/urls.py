from django.urls import path
from . import views

urlpatterns = [
    path('sendFeedback', views.sendFeedback, name='sendFeedback'),
]
