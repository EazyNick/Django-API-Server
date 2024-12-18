from django.http import HttpResponse
from .models import *
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello, world.")

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] # 최근 질문 5개 가져오기
#     context = {'first_question': latest_question_list[0]} # 첫번쨰 질문 1개
#     return render(request, 'polls/index.html', context)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    #context = {'questions': []}
    return render(request, 'polls/index.html', context)

def some_url(request):
    return HttpResponse("Some ulr을 구현해 봤습니다.")

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})