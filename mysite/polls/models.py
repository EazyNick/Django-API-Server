from django.db import models

"""
1. 모델 생성
2. 모델을 테이블에 써 주기 위한 마이그레이션이라는 걸 만든다. (python manage.py makemigrations polls)
마이그레이션이란?
**마이그레이션(Migration)**은 Django 모델의 변경 사항(예: 새 모델 추가, 기존 모델 수정)을 데이터베이스에 반영하기 위한 단계
3. 이 모델에 맞는 테이블을 만든다. (python manage.py migrate)
polls/migrations/0001_initial.py 파일을 읽고 데이터베이스에 테이블을 생성
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200) # 최대 길이 200의 char 필드 생성
    pub_date = models.DateTimeField('date published') # datetime 필드 생성 (질문 생성 날짜)

class Choice(models.Model):
    # ForeignKey - 한 테이블의 특정 필드가 다른 테이블의 행을 참조한다는 것을 의미, Question과 연결, 
    # on_delete: 외래 키가 참조하는 객체가 삭제될 때의 동작을 정의
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question 저장, Question 유니크한 ID를 저장, 참조된 객체가 삭제되면, 외래 키를 가진 객체도 삭제
    choice_text = models.CharField(max_length=200) # 선택한 선택지 저장
    votes = models.IntegerField(default=0) # 몇개의 투표를 받았는지 저장, 숫자로 저장
