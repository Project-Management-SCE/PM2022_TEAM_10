from django.urls import path

from . import views

urlpatterns = [
    path("", views.adminPanel, name="adminPanel"), # View 1 
    path("helpo_users", views.helpo_users, name="helpo_users"), # View 2
    path("manager_users", views.manager_users, name="manager_users"), # View 3
    path("AdminUpdateHelpoUser/<str:pk>/", views.AdminUpdateHelpoUser, name="AdminUpdateHelpoUser"), # View 1 
]
