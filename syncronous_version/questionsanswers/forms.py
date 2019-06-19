from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Question, Answer

class NewQuestionForm(forms.ModelForm):
    message = forms.CharField(
            widget = forms.Textarea(),
            max_length = 4000,
            label = "Descripción",
            help_text = "Límite: 4000 caracteres."
            )

    class Meta:
        model = Question
        fields = ['title', 'message']
        labels = {
            'title': _('Título')
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['message', ]
