from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from questions import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^courses/', views.CourseListView.as_view()),
    url(r'^questions/', views.QuestionListView.as_view()),
    url(r'^majors/', views.MajorListView.as_view()),
]
