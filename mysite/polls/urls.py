from django.urls import path
from . import views

# % url 'polls:detail' question.id % 처럼, 나중에 detail 이라는 이름의 url이 많아질 수 있으니, polls의 detail이라는 것을 명시하기 위해 사용
app_name = 'polls'

urlpatterns = [
    path('',views.index, name='index'), #polls 외에 파라미터로 아무것도 안붙어서 들어올 경우
    path('some_url',views.some_url),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'), 
]
