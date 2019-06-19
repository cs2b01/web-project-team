from django.utils                   import timezone
from django.db.models               import Count
from django.views.generic           import UpdateView
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts               import render, get_object_or_404, redirect
from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger

from .models import Subject, Question, Answer, User

from .forms import NewQuestionForm, AnswerForm

def all_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'all_subjects.html', {'subjects': subjects})

def questions_per_subject(request, pk):
    subject = get_object_or_404(Subject, pk = pk)
    queryset = subject.questions.order_by('-last_updated').annotate(replies = Count('answers') - 1)
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, "questions_per_subject.html", {'subject': subject, 'questions': questions})

@login_required
def new_question(request, pk):
    subject = get_object_or_404(Subject, pk = pk)
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.subject = subject
            question.starter = request.user
            question.save()
            answer = Answer.objects.create(
                message=form.cleaned_data.get('message'),
                question=question,
                created_by=request.user
            )
            return redirect('questions_per_subject', pk = subject.pk)
    else:
        form = NewQuestionForm()
    return render(request, 'new_question.html', {'subject': subject, 'form': form})


@login_required
def reply_question(request, pk, question_pk):
    question = get_object_or_404(Question, subject__pk = pk, pk=question_pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.created_by = request.user
            answer.save()

            question.last_updated = timezone.now()
            question.save()

            return redirect('answers_per_question', pk=pk, question_pk=question_pk)
    else:
        form = AnswerForm()
    return render(request, 'reply_question.html', {'question': question, 'form': form})


def answers_per_question(request, pk, question_pk):
    question = get_object_or_404(Question, subject__pk = pk, pk=question_pk)
    question.views += 1
    question.save()
    return render(request, 'answers_per_question.html', {'question': question})



@method_decorator(login_required, name='dispatch')
class AnswerUpdateView(UpdateView):
    model = Answer
    fields = ('message',)
    template_name = 'edit_answer.html'
    pk_url_kwarg = 'answer_pk'
    context_object_name = 'answer'

    def form_valid(self, form):
        answer = form.save(commit = False)
        answer.updated_by =  self.request.user
        answer.updated_at = timezone.now()
        answer.save()
        return redirect('answers_per_question', pk = answer.question.subject.pk, question_pk = answer.question.pk)

# !1| Static !1|

def static_faq(request):
    return render(request, "faq.html")

def static_contact(request):
    return render(request, "contact.html")
