from django.urls import path
from . import views

urlpatterns = [
    path("logout", views.logout, name="logout"),
    path('ManagerSignup', views.AssociationManagerSignUp.as_view(), name='ManagerSignup'),
    path('HelpoUserSignup', views.HelpoUserSignUp.as_view(), name='HelpoUserSignup'),
    path('pickType', views.pickType, name='pickType'),
    path('updateAssociationManager/<str:pk>/', views.updateAssociationManager,name='updateAssociationManager'),
    path('updateHelpoUser/<str:pk>/', views.updateHelpoUser,name='updateHelpoUser')
]
