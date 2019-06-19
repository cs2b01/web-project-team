from django.test import TestCase
from django.urls import reverse, resolve

from ..views import all_subjects, questions_per_subject, new_question

from ..forms import NewQuestionForm

from ..models import Subject, User, Question, Answer

class HomeTests(TestCase):
    def setUp(self):
        self.subject = Subject.objects.create(name = "Química general", description = 'El curso de química es muy divertido')
        url = reverse('home')
        self.response = self.client.get(url)
    """
    Testing if the homepage returns a successful status code. That is, it returns something that is not considered an error.
    """
    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    """
    Testing if Django is returning the page that contains all the subjects when going into '/'.
    TODO: The function must return the page that shows all the answers
    """
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        
        self.assertEquals(view.func, all_subjects)

    """
    Testing if the home view contains the reference to the website that shows the questions from a given subject.
    """
    def test_home_view_contains_links_to_questions_page(self):
        questions_from_a_given_subject = reverse('questions_per_subject', kwargs = {'pk': self.subject.pk})
        
        self.assertContains(self.response, 'href="{0}"'.format(questions_from_a_given_subject))


class SubjectQuestionsTests(TestCase):
    def setUp(self):
        subject = Subject.objects.create(name = "Química general", description = 'El curso de química es muy divertido')
    """
    Testing if Django is returning a status code 200 (success) for an existing Subject.
    """
    def test_subject_questions_view_success_status_code(self):
        url = reverse('questions_per_subject', kwargs = {'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    """
    Testing if Django is returning  a status code 404 (page not found) for a Subject that doesn't exist in the database.
    """

    def test_subject_questions_view_not_found_status_code(self):
        url = reverse('questions_per_subject', kwargs = {'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    """
    Testing if Django is using the correct view function to render the questions for a given ID from a subject.
    """
    def test_subject_url_resolves_questions_per_subject(self):
        view = resolve('/subjects/1/')
        self.assertEquals(view.func, questions_per_subject)

    """
    Testing if the homepage that shows all the questions for each subject contains links to create a new question and to go back to the list of subjects.
    """
    def test_questions_per_subject_view_contains_navigation_links(self):
        url_questions_per_subject = reverse('questions_per_subject', kwargs = {'pk': 1})
        url_homepage = reverse('home')
        url_new_question = reverse('new_question', kwargs = {'pk': 1})

        response = self.client.get(url_questions_per_subject)

        self.assertContains(response, 'href="{0}"'.format(url_homepage))
        self.assertContains(response, 'href="{0}"'.format(url_new_question))

class NewQuestionTests(TestCase):
    def setUp(self):
        Subject.objects.create(name = "Química general", description = 'El curso de química es muy divertido')
        User.objects.create(username = 'Rodrigo', email = 'rodrigo.morales@utec.edu.pe', password = 'fireman90')

    """
    Testing if the request to the view is succesful
    """
    def test_new_question_view_success_status_code(self):
        url = reverse('new_question', kwargs = {'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    """
    Testing if creating a new question for an unexisting subject returns a 404 code.
    """
    def test_new_question_view_not_found_status_code(self):
        url = reverse('new_question', kwargs = {'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    """
    Testing if entering into /subjects/1/new/ activates the function that allows to create a new question.
    """
    def test_new_question_url_resolves_new_topic_view(self):
        view = resolve('/subjects/1/new/')
        self.assertEquals(view.func, new_question)

    """
    Testing if creating a new question for a given subject contains the link that goes back to the website that shows all the questions for a given subject.
    """
    def test_new_question_view_contains_link_back_to_subject_questions_vie(self):
        new_question_for_a_given_subject_url = reverse('new_question', kwargs = {'pk': 1})
        questions_per_subject_url = reverse('questions_per_subject', kwargs = {'pk': 1})
        response = self.client.get(new_question_for_a_given_subject_url)
        
        self.assertContains(response, 'href="{0}"'.format(questions_per_subject_url))
    
    """
    Testing if the form contains a csrf token
    """
    def test_csrf(self):
        url = reverse('new_question', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    """
    Testing if a valid post data make Django create new objects
    """

    def test_new_topic_valid_post_data(self):
        url = reverse('new_question', kwargs = {'pk': 1})
        data = {
                'title': 'Testing question',
                'message': 'What is this question?'
                }
        response = self.client.post(url, data)
        self.assertTrue(Question.objects.exists())
        self.assertTrue(Answer.objects.exists())
    
    """
    Testing if invalid post data make Django not to redirect.
    The expected behavior is to show the form again with validation errors
    """
    def test_new_question_invalid_post_data(self):
        url = reverse('new_question', kwargs={'pk': 1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_new_question_invalid_post_data_empty_fields(self):
        url = reverse('new_question', kwargs={'pk': 1})
        data = {
            'title': '',
            'message': ''
        }
        response = self.client.post(url, data)

        self.assertEquals(response.status_code, 200)
        self.assertFalse(Question.objects.exists())
        self.assertFalse(Answer.objects.exists())

    def test_contains_form(self):
        url = reverse('new_question', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewQuestionForm)

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_question', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
