from django.urls import path
from django.shortcuts import redirect
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
path('', RedirectView.as_view(url='/thome/')),
path('thome/', views.thome, name='thome'),
path('thome/myexam/', views.myexam, name='myexam'),
path('thome/profile/', views.profile, name='profile'),
path('thome/teacher_req/', views.teacher_req, name='teacher_req'),
path('thome/student_list/', views.student_list, name='student_list'),
path('thome/assignment/', views.teacher_assignment_list, name='teacher_assignment_list'),
path('thome/exam_form/', views.exam_form, name='exam_form'),
path('thome/assignment_ques_form/', views.assignment_ques_form, name='assignment_ques_form'),
path('thome/profile/update/', views.profile_update, name='profile_update'),

]
