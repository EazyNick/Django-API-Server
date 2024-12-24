from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

"""
1. 모델 생성
2. 모델을 테이블에 써 주기 위한 마이그레이션이라는 걸 만든다. (python manage.py makemigrations polls)
마이그레이션이란?
**마이그레이션(Migration)**은 Django 모델의 변경 사항(예: 새 모델 추가, 기존 모델 수정)을 데이터베이스에 반영하기 위한 단계
3. 이 모델에 맞는 테이블을 만든다. (python manage.py migrate)
polls/migrations/0001_initial.py 파일을 읽고 데이터베이스에 테이블을 생성
"""

# class Question(models.Model):
#     question_text = models.CharField(max_length=200) # 최대 길이 200의 char 필드 생성
#     pub_date = models.DateTimeField(auto_now_add=True) # 시간 자동 등록
#     pub_date = models.DateTimeField('date published') # datetime 필드 생성 (질문 생성 날짜)
#     #is_something = models.BooleanField(default=False) # 불 값 필드, default=초기값
#     #average_score = models.FloatField(default=0.0) # 소수값 필드
#     # python manage.py migrate polls 0001, 위에 2가지를 추가하고 마이그레이션하면 0002가 생기는데, 0001로 되돌리고, 변경 코드를 지워주면 다시 돌아감 

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='질문')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일') 
    # 여러 개의 Question 객체가 하나의 User 객체에 연결될 수 있습니다.
    # 각 질문이 어느 사용자(auth.User)에 의해 생성되었는지를 나타냅니다.
    # related_name은 외래 키로 연결된 모델에서 이 관계를 역참조할 때 사용할 이름을 정의, user.questions.all(), 설정하지 않으면 question_set으로 가져옴
    owner = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE, null=True)

    # 이거는 정의된게 아니라, 함수로 구현된 것이기 때문에 데코레이터 사용
    # boolean=True - 최근 생성인 경우 체크표시, 아닌경우 X 아이콘으로 나옴
    @admin.display(boolean=True, description='최근생성(하루기준)')
    def was_published_recently(self):
        """
        최근에 생성된 Question 데이터인지 알아보기 
        
        return:
            Bool: 최근에 생성된 데이터 여부
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 이게 없으면 디폴트 값으로 값이 저장되어, 우리가 만든 값이 무엇인지 알기가 어려워서, 이름을 지정할 수 있다.
    def __str__(self):
        # 최근에 생성된 데이터라면 NEW 뱃지 붙여주기.
        if self.was_published_recently():
            new_badge = 'NEW!!!'
        else:
            new_badge = ''
        return f'{new_badge} 제목: {self.question_text}, 날짜: {self.pub_date}'

class Choice(models.Model):
    # ForeignKey - 한 테이블의 특정 필드가 다른 테이블의 행을 참조한다는 것을 의미, Question과 연결, 
    # on_delete: 외래 키가 참조하는 객체가 삭제될 때의 동작을 정의
    # question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question 저장, Question 유니크한 ID를 저장, 참조된 객체가 삭제되면, 외래 키를 가진 객체도 삭제
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) # 선택한 선택지 저장
    votes = models.IntegerField(default=0) # 몇개의 투표를 받았는지 저장, 숫자로 저장

    def __str__(self):
        return self.choice_text

    # def __str__(self):
    #     return f'[{self.question.question_text}] {self.choice_text}' # 질문, 선택지 다 보이게 바꿈

from django.contrib.auth.models import User

class Vote(models.Model):
    """
    투표 기능
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'voter'], name='unique_voter_for_questions')
        ]