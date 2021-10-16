from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('', HomePage, name='main'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('createsurvey/', createSurvey, name='createsurvey'),
    path('delete_survey/<int:survey_id>', deleteSurvey, name='delete_survey'),
    path('update_survey/<int:survey_id>', updateSurvey, name='update_survey'),
    path('addanswer/<int:question_id>', AddAnswer, name='add_answer'),
]