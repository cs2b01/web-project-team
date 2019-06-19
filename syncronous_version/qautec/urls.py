"""
!1| Todo !1|

!2| Higher priority !2|

- User authentication.
- Show all the questions in the homepage.
- Homepage for each user

!2| Less priority !2|

FAQ website
About website
"""

from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from questionsanswers import views
from accounts import views as accounts_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.all_subjects, name = 'home'),
    url(r'^faq/', views.static_faq),
    url(r'^contact/', views.static_contact),

    url(r'^subjects/(?P<pk>\d+)/$', views.questions_per_subject, name='questions_per_subject'),
    url(r'^subjects/(?P<pk>\d+)/questions/(?P<question_pk>\d+)/$', views.answers_per_question, name='answers_per_question'),
    url(r'^subjects/(?P<pk>\d+)/questions/(?P<question_pk>\d+)/reply/$', views.reply_question, name='reply_question'),

    url(r'^subjects/(?P<pk>\d+)/new/$', views.new_question, name='new_question'),
    url(r'^subjects/(?P<pk>\d+)/questions/(?P<question_pk>\d+)/answers/(?P<answer_pk>\d+)/edit/$', views.AnswerUpdateView.as_view(), name='edit_answer'),

    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #FIX THIS PROBLEM: Why on earth does "accounts/" is included in the URI when login is required and the user is not logged.
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    url(r'^reset/$',                                                                            auth_views.PasswordResetView.as_view            (template_name='password_reset/base.html', email_template_name='password_reset/email.html', subject_template_name='password_reset/subject.txt'), name='password_reset'),
    url(r'^reset/done/$',                                                                       auth_views.PasswordResetDoneView.as_view        (template_name='password_reset/done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view     (template_name='password_reset/confirm.html'), name='password_reset_confirm'),
    url(r'^reset/complete/$',                                                                   auth_views.PasswordResetCompleteView.as_view    (template_name='password_reset/complete.html'), name='password_reset_complete'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change/process.html'),               name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change/done.html'), name='password_change_done'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
]
