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

# def detail(request, question_id):
#     question = Question.objects.get(pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render , get_object_or_404
from django.urls import reverse

...
def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    # 위 코드를 간략화 하는 방법임 - get_object_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
# Choice.DoesNotExist는, 삭제된 데이터를 투표했을 경우 에러 메시지 출력
#     except (KeyError, Choice.DoesNotExist): # 아무것도 choice하지 않은 경우
#         return render(request, 'polls/detail.html', {'question': question, 'error_message': '선택이 없습니다.'})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:index'))
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': f"선택이 없습니다. id={request.POST['choice']}"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))