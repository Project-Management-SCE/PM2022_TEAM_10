from django.urls import path
from . import views



urlpatterns = [
    path('createReportPost/<str:pk>', views.createReportPost, name='createReportPost'),

]