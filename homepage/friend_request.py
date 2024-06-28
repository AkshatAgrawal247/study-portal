from django.db import models
from django.contrib.auth.models import User
from student.models import Stud
from teacher.models import Tutor

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from homepage.decorators import allowed_users


class FriendRequest(models.Model):
	to_user = models.ForeignKey(Tutor, related_name='to_user' ,on_delete=models.CASCADE)
	from_user = models.ForeignKey(Stud, related_name='from_user', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return "From {}, to {}".format(self.from_user, self.to_user)


@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def send_friend_request(request, id):
	teacher = Tutor.objects.get(id=id)
	student = request.user.stud
	frequest, created = FriendRequest.objects.get_or_create(
		from_user=student,
		to_user=teacher)
	return redirect('/shome/student_req')

@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['student'])
def cancel_friend_request(request, id):
	teacher = Tutor.objects.filter(id=id).first()
	student = request.user.stud
	frequest = FriendRequest.objects.filter(
		from_user=student,
		to_user=teacher).first()
	frequest.delete()
	return redirect('/shome')

@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def accept_friend_request(request, id):
	from_user = Stud.objects.filter(id=id).first()
	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user.tutor).first()
	teacher = frequest.to_user
	student = from_user
	teacher.friends.add(student)
	frequest.delete()
	return redirect('/thome')

@login_required(login_url='/home/login')
@allowed_users(allowed_roles=['teacher'])
def delete_friend_request(request, id):
	from_user = Stud.objects.filter(id=id).first()
	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user.tutor).first()
	frequest.delete()
	return redirect('/thome')
