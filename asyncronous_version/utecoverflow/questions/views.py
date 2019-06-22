from questions.models import Course, Major, Question, User
from questions.serializers import CourseListSerializer, QuestionListSerializer, QuestionDetailSerializer, MajorListSerializer
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CourseListView(APIView):

    def get_queryset(self):
        return Course.objects.all()

    def get(self, request):
        serializer = CourseListSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.saver()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionListView(APIView):

    def get_queryset(self):
        return Question.objects.all()

    def get(self, request):
        serializer = QuestionListSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class QuestionDetailView(APIView):

    def get_queryset(self):
        return Question.objects.get(id=self.request.id)

    def get(self, request):
        serializer = QuestionDetailSerializer(self.get_queryset())
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionDetailSerializer(self.get_queryset())
        return Response(serializer.data)

class MajorListView(APIView):

    def get_queryset(self):
        return Major.objects.all()

    def get(self, request):
        serializer = MajorListSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

