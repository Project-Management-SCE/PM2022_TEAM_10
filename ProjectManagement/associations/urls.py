from django.urls import path
from . import views

urlpatterns = [
    path('All', views.All, name='All'),
    path("profile/<str:pk>/", views.profile, name="profile"),  
    path("profile/<str:pk>/volunteerRequest", views.submitVolunteeringRequest, name="submitVolunteeringRequest"),  
    path("profile/<str:pk>/volunteersRequests", views.volunteersRequests, name="volunteersRequests"),
    path("profile/<str:pk>/volunteersRequests/<str:r_pk>", views.showRequest, name="showRequest"),
    path("deleteVolRequest/<str:pk>", views.deleteVolRequest, name="deleteVolRequest"),
]