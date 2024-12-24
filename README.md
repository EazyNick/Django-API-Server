# Django Polls 프로젝트

이 저장소는 Django 기반의 투표 애플리케이션을 단계적으로 구현한 코드입니다. 학습 과정은 다음 블로그 포스트를 참고하여 진행되었습니다:

- [1단계: Django 설정 및 모델 생성](https://kimsungjun9987.tistory.com/458)
- [2단계: Serializer 및 API 추가](https://kimsungjun9987.tistory.com/459)

---

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [주요 기능](#주요-기능)
3. [설치 및 설정](#설치-및-설정)
4. [학습 단계](#학습-단계)
   - [1단계: Django 설정 및 모델 생성](#1단계-django-설정-및-모델-생성)
   - [2단계: Serializer 및 API 추가](#2단계-serializer-및-api-추가)
5. [실행 방법](#실행-방법)

---

## 프로젝트 개요

이 프로젝트는 간단한 투표 애플리케이션으로, 사용자가 질문을 생성하고, 선택지에 투표하며, 투표 결과를 확인할 수 있는 기능을 제공합니다. Django 초보자를 대상으로 다음을 학습하는 데 중점을 둡니다:
- Django 프로젝트 및 애플리케이션 설정.
- 모델, Serializer, 뷰(View) 활용법.
- Django REST Framework(DRF)를 사용한 RESTful API 구축.

---

## 주요 기능
1. **투표 생성**: 사용자가 투표 질문과 선택지를 생성할 수 있습니다.
2. **투표 참여**: 사용자가 선택지에 투표할 수 있습니다.
3. **투표 결과**: 실시간으로 투표 결과를 확인할 수 있습니다.
4. **REST API**: DRF를 사용한 완전한 API 제공.

---

## 설치 및 설정

1. 이 저장소를 클론합니다:
   ```bash
   git clone https://github.com/yourusername/django-polls.git
   cd django-polls
    ```

2. 필요한 라이브러리를 설치합니다:
    ```bash
    pip install -r requirements.txt
    ```

3. 데이터베이스 마이그레이션을 적용합니다:
    ```bash
    python manage.py migrate
    ```

4. 개발 서버를 실행합니다:
    ```bash
    python manage.py runserver
    ```

## 학습 단계

### 1단계: Django 설정 및 모델 생성
**커밋 참조:** `initial-setup-and-models`

1. Django를 설치하고, 새 프로젝트(`polls_project`)와 앱(`polls`)을 생성했습니다.

2. **`Question`, `Choice`, `Vote` 모델을 정의했습니다:**
- **`Question`**: 투표 질문과 생성일을 저장합니다.
- **`Choice`**: 각 질문에 연결된 선택지를 저장합니다.
- **`Vote`**: 특정 사용자가 어떤 선택지에 투표했는지를 기록합니다.

**관련 코드:**
```python
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
```

3. 데이터베이스에 테이블을 생성하기 위해 마이그레이션을 적용했습니다.

---

### 2단계: Serializer 및 API 추가
**커밋 참조:** `serializers-and-apis`

1. Django REST Framework(DRF)를 설치하여 RESTful API를 구축했습니다.

2. **`Question`, `Choice`, `Vote` 모델을 위한 Serializer를 생성했습니다:**
- **`QuestionSerializer`**: 질문 데이터를 처리합니다.
- **`ChoiceSerializer`**: 선택지 데이터를 처리합니다.
- **`VoteSerializer`**: 투표 데이터를 처리합니다.

**관련 코드:**
```python
class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'owner']

3. API 뷰를 추가했습니다:

- **`ListCreateAPIView`**를 사용해 질문 리스트와 생성 기능을 추가했습니다.
- **`RetrieveUpdateDestroyAPIView`**를 사용해 질문 조회, 수정, 삭제 기능을 추가했습니다.
- `perform_create` 메서드를 오버라이딩하여 요청한 사용자를 `owner` 필드에 연결했습니다.
- Postman 또는 DRF의 내장 브라우저 UI를 통해 API를 테스트했습니다.

---

## 실행 방법

### 개발 서버를 실행합니다:
```bash
python manage.py runserver
```

## 브라우저 또는 API 클라이언트를 통해 다음 엔드포인트를 확인하세요:

- **`GET /api/questions/`**: 모든 질문 리스트를 조회합니다.
- **`POST /api/questions/`**: 새로운 질문을 생성합니다(인증 필요).
- **`GET /api/questions/<id>/`**: 특정 질문의 상세 정보를 조회합니다.
- **`POST /api/votes/`**: 선택지에 투표합니다(인증 필요).

---

## 참고 사항

- 이 프로젝트는 학습 목적으로 설계되었으며, 보안 및 성능 최적화는 포함되어 있지 않습니다.
- 추가 기능: 사용자 인증, 페이지네이션, 데이터 유효성 검증 등을 구현할 수 있습니다.

---

## 참고 자료

- [Django 공식 문서](https://docs.djangoproject.com/)
- [Django REST Framework 공식 문서](https://www.django-rest-framework.org/)
