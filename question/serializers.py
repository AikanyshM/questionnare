from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Question, Answer, Result

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


    def create(self, validated_data):
        user = User(username=validated_data['username']),
        is_staff=validated_data['is_staff']
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        
    def validate(self, data):
        if data['question']:
            question = data['question']
            if question.type == "Текст":
                raise serializers.ValidationError('У данного вопроса тип текст')
        return data

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['question', 'answer']
        read_only_fields = ['user']

    def validate(self, data):
        if data['question']:
            question = data['question']
            answer = data['answer']
            if question.type == "Выбор":
                if not Answer.objects.filter(question=question, text=answer).exists():
                    raise serializers.ValidationError('У данного вопроса тип "выбор". Ответ не из выбора')
        return data


            
