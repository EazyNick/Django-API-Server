from rest_framework.decorators import api_view
from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])  # http요청 허용, 지정하지 않았으니 모든 http 요청을 허용(get, post 등)
def question_list(request):
    """
    API 엔드포인트로 동작하는 함수
    """
    if request.method == 'GET': # 모든 Question 목록 조회
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many = True) # json으로 변환(직렬화)
        return Response(serializer.data) # 클라이언트에 JSON 형식의 응답을 반환
    
    if request.method == 'POST': # Questiong 등록
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 에러기 때문에 400으로 해줘야함.

"""
데이터 생성(Create) : POST
데이터 조회(Read) : GET
데이터 업데이트(Update) : PUT
데이터 삭제(Delete) : DELETE
"""