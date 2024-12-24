from rest_framework import serializers
from polls.models import Question

from rest_framework import serializers
from polls.models import Question

from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
    """
    만들어진 모델이 있다면, 더 쉽게 불러올 수 있다.
    """
    class Meta:
        model = Question
        fields = ['id','question_text', 'pub_date']

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'questions']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "두 패스워드가 일치하지 않습니다."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    class Meta:
        model = User
        fields = ['username', 'password','password2']

# class QuestionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True) # 클라이언트가 데이터를 제공할 수 없게 함(read_only)
#     question_text = serializers.CharField(max_length=200)
#     pub_date = serializers.DateTimeField(read_only=True)

#     # validated_data는 입력된 데이터가 유효성 검사를 통과한 후 제공됨
#     def create(self, validated_data):
#         """
#         예시: serializer = QuestionSerializer(data=data)
#         """
#         return Question.objects.create(**validated_data)

#     # instance는 기존의 Question 모델 인스턴스
#     def update(self, instance, validated_data):
#         """
#         예시: serializer = QuestionSerializer(new_question, data=data)
#         """
#         instance.question_text = validated_data.get('question_text', instance.question_text)
#         instance.save()
#         return instance
    