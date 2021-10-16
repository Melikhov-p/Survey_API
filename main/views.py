import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def HomePage(request):
    context = {
        'title':'главная',
        'choices': Choice.objects.all().order_by('id'),
        'Questions': Question.objects.filter(survey__end_date__gt=datetime.datetime.now()), #Отдаем только те опросы у которых дата окончания больше, чем ныняшняя дата
    }
    if request.user.is_authenticated:
        context['answers'] = Answer.objects.filter(user_id=request.user.id)

    return render(request, 'index.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        context = {
            'form': UserLoginForm(),
        }
        return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('main')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        context = {
            'form': UserRegisterForm()
        }
        return render(request, 'register.html', context)

def createSurvey(request):
    if request.method == 'GET':
        context = {
            'form': CreateSurveyForm,
        }
        return render(request, 'createsurvey.html', context)
    else:
        form = CreateSurveyForm(request.POST)
        if form.is_valid():
            form.cleaned_data['question_type'] = request.POST.get('question_type')
            form.cleaned_data['question_text'] = request.POST.get('question_text')
            Survey.objects.create(survey_name=form.cleaned_data['survey_name'], survey_description=form.cleaned_data['survey_description'], end_date=form.cleaned_data['end_date'])#Создаем запись опроса
            Question.objects.create(survey=Survey.objects.get(survey_name=form.cleaned_data['survey_name']), question_text=form.cleaned_data['question_text'], question_type=form.cleaned_data['question_type'])#Создаем запись вопроса
            if request.POST.get('question_type') == '2' or request.POST.get('question_type') == '3':#Если тип вопроса подразумевает выбор ответа или нескольких - то создаем записи выборов
                for i in range(1, 11):
                    if request.POST.get('choice_'+str(i)) is None:
                        break
                    else:
                        Choice.objects.create(question=Question.objects.get(question_text=form.cleaned_data['question_text']), choice_text=request.POST.get('choice_'+str(i)))
            return redirect('main')

def deleteSurvey(request, survey_id): #Удаление опроса
    if request.user.is_superuser:
        Survey.objects.get(id=survey_id).delete()
        return redirect('main')
    else:
        return redirect('login')

def updateSurvey(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    question = Question.objects.get(survey_id=survey_id)
    if request.method == 'GET':
        form = UpdateSurveyForm()
        context = {
            'form':form,
            'survey': survey,
            'question': question,
        }
        if context['question'].question_type == '2' or context['question'].question_type == '3':
            context['choices'] = Choice.objects.filter(question_id=context['question'].id)
        return render(request, 'updatesurvey.html', context)
    else:
        form = UpdateSurveyForm(request.POST)
        if form.is_valid():
            survey.survey_name = request.POST.get('survey_name')
            survey.survey_description = request.POST.get('survey_description')
            survey.end_date = request.POST.get('end_date')
            survey.save()
            question.question_text = request.POST.get('question_text')
            if request.POST.get('question_type') != '0':
                question.question_type = request.POST.get('question_type')
            question.save()
            if question.question_type == '2' or question.question_type == '3':
                choices = Choice.objects.filter(question_id=question.id)
                for i in range(1, 11):
                    if request.POST.get('choice_' + str(i)) is None:
                        break
                    else:
                        choices[i-1].choice_text = request.POST.get('choice_' + str(i))
                        choices[i-1].save()
            return redirect('main')

def AddAnswer(request, question_id):
    question = Question.objects.get(id=question_id)
    if question.question_type == '1':
        Answer.objects.create(user_id=request.user.id, survey=question.survey, question=question, choice_text=request.POST.get('answer_input'))
    elif question.question_type == '2':
        choice = request.POST.getlist('choice')
        Answer.objects.create(user_id=request.user.id, survey=question.survey, question=question, choice=Choice.objects.filter(question_id=question.id, choice_text=choice[0])[0])
    else:
        choices = request.POST.getlist('choice')
        answer = Answer.objects.create(user_id=request.user.id, survey=question.survey, question=question)
        for choice in choices:
            answer.choice.add(Choice.objects.filter(question_id=question.id, choice_text=choice)[0])
    return redirect('main')