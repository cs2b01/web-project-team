from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Major(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=120)
    def __str__(self):
       return self.name

class User(AbstractUser):
    pass

class Course(models.Model):
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=120)
    
    def __str__(self):
       return self.name

class Question(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=120)
    current_score = models.IntegerField(default=0)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Question, self).save(*args, **kwargs)

class Answer(models.Model):
    content = models.CharField(max_length=400, default='')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
