from rest_framework.decorators import api_view
from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from django.contrib.auth.models import User
from polls_api.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Generic API View
# from polls.models import Question
# from polls_api.serializers import QuestionSerializer
# from rest_framework import generics

# class QuestionList(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# Mixin 기반 view 구현
# from polls.models import Question
# from polls_api.serializers import QuestionSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class QuestionList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class QuestionDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# Class 기반의 뷰(Views)
class QuestionList(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetail(APIView):
    def get(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        question = get_object_or_404(Question, pk=id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])  # http요청 허용, 지정하지 않았으니 모든 http 요청을 허용(get, post 등)
# def question_list(request):
#     """
#     API 엔드포인트로 동작하는 함수
#     """
#     if request.method == 'GET': # 모든 Question 목록 조회
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many = True) # json으로 변환(직렬화)
#         return Response(serializer.data) # 클라이언트에 JSON 형식의 응답을 반환
    
#     if request.method == 'POST': # Questiong 등록
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 에러기 때문에 400으로 해줘야함.

# @api_view(['GET', 'PUT', 'DELETE'])
# def question_detail(request, id):
#     question = get_object_or_404(Question, pk=id)
    
#     if request.method == 'GET':
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:    
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
데이터 생성(Create) : POST
데이터 조회(Read) : GET
데이터 업데이트(Update) : PUT
데이터 삭제(Delete) : DELETE
"""