from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'), #polls 외에 파라미터로 아무것도 안붙어서 들어올 경우
    path('some_url',views.some_url),
    path('<int:question_id>/', views.detail, name='detail'),
]
