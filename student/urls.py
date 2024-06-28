from django.urls import path
from django.shortcuts import redirect
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
path('', RedirectView.as_view(url='/shome/')),
path('shome/', views.shome, name='shome'),
path('shome/profile/', views.student_profile, name='student_profile'),
path('shome/profile/update', views.student_profile_update, name='student_profile_update'),
path('shome/teachers/', views.teachers, name='teachers'),
path('shome/myclasses/', views.myclasses, name='myclasses'),
path('shome/assignment/', views.student_assignment_list, name='student_assignment_list'),
path('shome/student_req/', views.student_req, name='student_req'),
path('shome/myclasses/<int:id>/', views.view_lecture, name='view_lecture'),
path('shome/assignment/<int:id>/', views.assignment_ans_form, name='assignment_ans_form'),
]