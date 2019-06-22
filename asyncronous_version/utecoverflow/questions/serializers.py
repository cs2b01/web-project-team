from rest_framework import serializers
from questions.models import Course, Question, Major, User
from django.conf import settings


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'description',)
    

class QuestionListSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('title', 'description', 'current_score', 'answers')


class QuestionDetailSerializer(serializers.ModelSerializer):
    major = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='Course-major_id')
    
    user_name = serializers.HyperlinkedRelatedField(
                many=True,
                read_only=True,
                view_name='User-name')


    class Meta:
        model = Question
        fields = ('title', 'description', 'current_score', 'user_id', 'major', 'user_name')

class MajorListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Major
        fields = ('name', 'description')
