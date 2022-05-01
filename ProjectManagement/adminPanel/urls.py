from django.urls import path

from . import views

urlpatterns = [
    path("", views.adminPanel, name="adminPanel"), # View 1 
    path("helpo_users", views.helpo_users, name="helpo_users"), # View 2
    path("manager_users", views.manager_users, name="manager_users"), # View 3
    path("posts", views.adminPosts, name="posts"), # View 3
    path("AdminPostDetails/<str:pk>/", views.AdminPostDetails, name="AdminPostDetails"), 
    path("AdminDeletePost/<str:pk>/", views.AdminDeletePost, name="AdminDeletePost"), 
    path("AdminUpdateHelpoUser/<str:pk>/", views.AdminUpdateHelpoUser, name="AdminUpdateHelpoUser"), 
    path("categories", views.categories, name="categories"),
    path("editCategory/<str:pk>/", views.editCategory, name="editCategory"), 
    path("deleteCategory/<str:pk>", views.deleteCategory, name="deleteCategory"),
    path("searchAssociation", views.searchAsso, name="searchAsso"),
]
