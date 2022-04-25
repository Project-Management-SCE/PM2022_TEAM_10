from django.urls import path
from . import views

urlpatterns = [
    path('All', views.All, name='All'),
    path("profile/<str:pk>/", views.profile, name="profile"),  
    path("profile/<str:pk>/volunteerRequest", views.submitVolunteeringRequest, name="submitVolunteeringRequest"),  
    path("profile/<str:pk>/volunteersRequests", views.volunteersRequests, name="volunteersRequests"),
]