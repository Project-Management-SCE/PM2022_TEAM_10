from django.urls import path

from . import views

urlpatterns = [
    path("logout", views.logout, name="logout"),
    path('signup', views.AssociationManagerSignUp.as_view(), name='AssociationManagerSignUp'),
    path('test', views.test, name='test')
    #  path('accounts/signup/association_manager/', association_manager.AssociationManagerSignUpView.as_view(), name='student_signup'),
]
