from rest_framework import serializers
from mroom.api.serializer.user import CurrentUserSerializer
from mroom.report.models import Survey, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'name',
            'description',
            'key'
        ]

    name = serializers.CharField()
    description = serializers.CharField()
    key = serializers.CharField()


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    solutions = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['answers', 'solutions']

class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    user = CurrentUserSerializer()

    class Meta:
        model = Survey
        fields = ['user', 'questions']