from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from homepage.decorators import allowed_users
from teacher.models import *
from .models import Stud
from homepage.friend_request import FriendRequest
from teacher.form import Assignment_ans_Form



@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def student_profile(request):
	return render(request, 'student_profile.html')

@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def student_req(request):
	requests = FriendRequest.objects.filter(from_user=request.user.stud)
	return render(request, 'student_req.html',{'requests':requests})
	

@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def teachers(request):
	teachers=Tutor.objects.exclude(friends=request.user.stud)
	return render(request, 'teachers.html',{'teachers':teachers})


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def myclasses(request):
	teachers=Tutor.objects.filter(friends=request.user.stud)
	return render(request, 'myclasses.html',{'teachers':teachers})


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def view_lecture(request,id):
	try:
		teacher=Tutor.objects.get(id=id, friends=request.user.stud)
		exams=Exam.objects.filter(teacher=teacher).order_by('date_created')
		return render(request, 'view_lecture.html',{'exams':exams,'teacher':teacher})
	except:
		return redirect('/shome/myclasses/') 


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def student_assignment_list(request):
	teachers=Tutor.objects.filter( friends=request.user.stud)
	assignments=Assignment_ques.objects.filter(teacher__in =teachers).order_by('date_created')
	return render(request, 'student_assignment_list.html',{'assignments':assignments})
	

@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def assignment_ans_form(request,id):
	teachers=Tutor.objects.filter(friends=request.user.stud)
	assignment_q=Assignment_ques.objects.get(id=id)
	if assignment_q.teacher in teachers:
		form = Assignment_ans_Form()
		if request.method == 'POST':
			form = Assignment_ans_Form(request.POST)
			if form.is_valid():
				form.save()
				assignment_q.students.add(request.user.stud)
				return redirect('/shome/assignment/')
		context ={'form':form}
		return render(request, 'assignment_ans_form.html',context)
	else:
		return redirect('/shome/assignment/') 




@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def student_profile_update(request):
	form = StudentProfileForm(instance=request.user.stud)
	if request.method == 'POST':
		form = StudentProfileForm(request.POST,instance=request.user.stud)
		if form.is_valid():
			form.save()
			return redirect('/shome/profile')
	
	context ={'form':form}
	return render(request, 'student_profile_form.html',context)



@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def shome(request):
	teachers=Tutor.objects.filter(friends=request.user.stud)
	requests = FriendRequest.objects.filter(from_user=request.user.stud)
	assignments=Assignment_ans.objects.filter(student =request.user.stud)
	
	no_of_request=requests.count()
	no_of_class=teachers.count()
	no_of_assignment=assignments.count()
	
	
	context={'no_of_assignment':no_of_assignment,
				'no_of_request':no_of_request,
				'no_of_class':no_of_class
				}

	return render(request, 'student_dashboard.html',context)