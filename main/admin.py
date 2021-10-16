from django.contrib import admin
from .models import *

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey_name', 'pub_date', 'end_date')
    search_fields = ('survey_name',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'question_text', 'question_type')
    search_fields = ('survey', 'question_text')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('survey', 'user_id', 'question', 'choice_text')
    search_fields = ('survey', 'user_id')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text')
    search_fields = ('question', 'choice_text')

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Choice, ChoiceAdmin)
