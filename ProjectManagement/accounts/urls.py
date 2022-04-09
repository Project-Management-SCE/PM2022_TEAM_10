from django.urls import path

from . import views

urlpatterns = [
    path("logout", views.logout, name="logout"),
    path('ManagerSignup', views.AssociationManagerSignUp.as_view(), name='ManagerSignup'),
    path('pickType', views.pickType, name='pickType')
    #  path('accounts/signup/association_manager/', association_manager.AssociationManagerSignUpView.as_view(), name='student_signup'),
]
