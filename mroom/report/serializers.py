from rest_framework import serializers

from mroom.api.serializer.user import CurrentUserSerializer
from mroom.report.models import Survey, Question, Answer, Report


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
    solutions = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'answers',
            'solutions',
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        del rep["questions"]["solutions"]
        return rep


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    user = CurrentUserSerializer()

    class Meta:
        model = Survey
        fields = ['user', 'questions']


class ReportSerializer(serializers.ModelSerializer):
    survey = SurveySerializer()

    class Meta:
        model = Report
        fields = ['survey']

        # REPORT FIELD


class ReportSurveyField(serializers.SlugRelatedField):
    def to_representation(self, survey):
        return ReportSerializer(survey).data


class ReportSurveySerializer(serializers.ModelSerializer):
    survey = ReportSurveyField(
        many=True,
        slug_field='key',
        queryset=Survey.objects.all()
    )


# QUESTION FIELD
class ReportQuestionField(serializers.SlugRelatedField):
    def to_representation(self, questions):
        return QuestionSerializer(questions).data


class ReportQuestionSerializer(serializers.ModelSerializer):
    questions = ReportQuestionField(
        slug_field='key',
        queryset=Survey.objects.all()
    )


# ANSWER FIELD
class ReportAnswerField(serializers.SlugRelatedField):
    def to_representation(self, answers):
        return AnswerSerializer(answers).data


class ReportAnswerSerializer(serializers.ModelSerializer):
    answers = ReportAnswerField(
        slug_field='key',
        queryset=Survey.objects.all(),
    )
