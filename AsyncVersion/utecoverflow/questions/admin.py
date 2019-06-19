from django.contrib import admin
from .models import User, Course, Question, Major, Answer

admin.register(User, Course, Question, Major, Answer)(admin.ModelAdmin)

class Major(admin.ModelAdmin):
    fields=('name','description')
    exclude = ('carreer_id')
