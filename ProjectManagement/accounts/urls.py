from django.urls import path
from . import views


urlpatterns = [
    path("logout", views.logout, name="logout"),
    # path("login", views.login_view, name="login"),
    path('ManagerSignup', views.AssociationManagerSignUp.as_view(), name='ManagerSignup'),
    path('HelpoUserSignup', views.HelpoUserSignUp.as_view(), name='HelpoUserSignup'),
    path('pickType', views.pickType, name='pickType'),
    path('updateAssociationManager/<str:pk>/', views.updateAssociationManager,name='updateAssociationManager'),
    path('updateHelpoUser/<str:pk>/', views.updateHelpoUser,name='updateHelpoUser'),
    path("helpo_porfile/<str:pk>", views.helpo_porfile, name="helpo_porfile")

]
