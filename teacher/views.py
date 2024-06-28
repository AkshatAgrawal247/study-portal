from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from homepage.decorators import allowed_users,teacher
from homepage.friend_request import FriendRequest


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def myexam(request):
    tutor  = request.user.tutor
    exams=Exam.objects.filter(teacher=tutor)
    assignments=Assignment_ques.objects.filter(teacher=tutor)
    return render(request, 'myexam.html',{'exams':exams,'assignments':assignments})




@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def profile(request):
    tutor = request.user.tutor
    return render(request, 'profile.html')


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def exam_form(request):
    tutor  = request.user.tutor
    form = ExamForm()
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thome/myexam')

    context ={'form':form}
    return render(request, 'exam_form.html',context)


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def assignment_ques_form(request):
    tutor  = request.user.tutor
    form = Assignment_ques_Form()
    if request.method == 'POST':
        form = Assignment_ques_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thome/myexam')

    context ={'form':form}
    return render(request, 'assignment_ques_form.html',context)


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def profile_update(request):
    form = ProfileForm(instance=request.user.tutor)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user.tutor)
        if form.is_valid():
            form.save()
            return redirect('/thome/profile')
    
    context ={'form':form}
    return render(request, 'profile_form.html',context)


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def teacher_req(request):
    requests = FriendRequest.objects.filter(to_user=request.user.tutor)
    return render(request, 'teacher_req.html',{'requests':requests})



@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def student_list(request):
    students = request.user.tutor.friends.all()
    return render(request, 'student_list.html',{'students':students})


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def teacher_assignment_list(request):
    teacher=request.user.tutor
    assignments=Assignment_ans.objects.filter(teacher =teacher)
    return render(request, 'teacher_assignment_list.html',{'assignments':assignments})
    
@login_required(login_url='/home/login')
@teacher
def thome(request):
    students = request.user.tutor.friends.all()
    exams=Exam.objects.filter(teacher=request.user.tutor)
    requests = FriendRequest.objects.filter(to_user=request.user.tutor)
    assignments=Assignment_ques.objects.filter(teacher =request.user.tutor)
    no_of_student=students.count()
    no_of_lecture=exams.count()
    no_of_request=requests.count()
    no_of_assignment=assignments.count()
    context={'no_of_assignment':no_of_assignment,
                'no_of_request':no_of_request,
                'no_of_lecture':no_of_lecture,
                'no_of_student':no_of_student,
                'assignments':assignments,
                'students':students}

    return render(request, 'teacher_dashboard.html',context)
