from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

"""
데이터 생성(Create) : POST
데이터 조회(Read) : GET
데이터 업데이트(Update) : PUT
데이터 삭제(Delete) : DELETE
"""

@api_view() # http요청 허용, 지정하지 않았으니 모든 http 요청을 허용(get, post 등) - @api_view(['GET'])
def question_list(request):
    """
    API 엔드포인트로 동작하는 함수

    """
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many = True) # json으로 변환(직렬화)
    return Response(serializer.data) # 클라이언트에 JSON 형식의 응답을 반환