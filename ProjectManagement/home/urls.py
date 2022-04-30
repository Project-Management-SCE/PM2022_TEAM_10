from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # View 1 
    # path("categories", views.createCategory, name="createCategory"), 
    # path("editCategory/<str:pk>/", views.editCategory, name="editCategory"), 
    # path("deleteCategory/<str:pk>", views.deleteCategory, name="deleteCategory"),

    
]
