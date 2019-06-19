from django.urls import reverse, resolve

from django.test import TestCase

from questionsanswers.models import User
from ..views import signup
from ..forms import MyUserCreationForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = MyUserCreationForm()
        expected = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
