from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

"""
!1| Markdown rendering !1|
"""

from markdown import markdown
from django.utils.html import mark_safe

"""
Subjects must not be unique, since some subjects from some courses must have the same name. For instance, "Discrete mathematics" must have the same subject "logic gates" as the course "Analog circuits" from the major "Mechatronics engineering."
"""

class Subject(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    def get_answers_count(self):
        return Answer.objects.filter(question__subject=self).count()

    def get_last_answer(self):
        return Answer.objects.filter(question__subject=self).order_by('-created_at').first()

class Question(models.Model):
    title = models.CharField(max_length = 255)
    last_updated = models.DateTimeField(auto_now_add = True)
    subject = models.ForeignKey(Subject, related_name = 'questions', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name = 'questions', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_last_ten_answers(self):
        return self.answers.order_by('-created_at')[:10]

class Answer(models.Model):
    message = models.TextField(max_length = 4000)
    question = models.ForeignKey(Question, related_name = 'answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(null = True)
    created_by = models.ForeignKey(User, related_name = 'answers', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null = True, related_name = '+', on_delete=models.CASCADE)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode = 'escape'))
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
