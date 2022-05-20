from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # View 1 
    path("QuestionsAndAnswers", views.QuestionsAndAnswers, name="QuestionsAndAnswers"), # View 1

]
