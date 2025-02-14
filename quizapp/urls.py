from django.contrib import admin
from django.urls import path
from . import views
urlpatterns =[
    path('',views.quizapp,name='quizapp'),
    path('quiz/',views.quiz,name='quiz'),
    path('api/get-quiz/',views.get_quiz,name='get_quiz')
]