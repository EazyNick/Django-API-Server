from rest_framework import serializers
from polls.models import Question

class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # 클라이언트가 데이터를 제공할 수 없게 함(read_only)
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField(read_only=True)

    # validated_data는 입력된 데이터가 유효성 검사를 통과한 후 제공됨
    def create(self, validated_data):
        """
        예시: serializer = QuestionSerializer(data=data)
        """
        return Question.objects.create(**validated_data)

    # instance는 기존의 Question 모델 인스턴스
    def update(self, instance, validated_data):
        """
        예시: serializer = QuestionSerializer(new_question, data=data)
        """
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.save()
        return instance
    