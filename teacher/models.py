from django.db import models
from django.contrib.auth.models import User
from student.models import Stud

class Tutor(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True,default='test teacher')
    phone=models.CharField(max_length=200, null=True,default='1234')
    email= models.CharField(max_length=200, null=True,default='name@mail')
    friends = models.ManyToManyField(Stud, blank=True)

    def __str__(self):
        return self.name


class Exam(models.Model):
    teacher=models.ForeignKey(Tutor, null=True, on_delete=models.SET_NULL)
    tittle=models.CharField(max_length=200, null=False)
    date_created=models.DateTimeField(auto_now_add=True, null =True)
    description = models.TextField(default='this id your lecture, document type lecture')

    def __str__(self):
        return self.tittle


class Assignment_ques(models.Model):
    teacher=models.ForeignKey(Tutor, null=True, on_delete=models.SET_NULL)
    students=models.ManyToManyField(Stud, blank=True)
    tittle=models.CharField(max_length=200, null=False)
    date_created=models.DateTimeField(auto_now_add=True, null =True)
    description = models.TextField(default='this id your lecture, document type lecture')

    def __str__(self):
        return self.tittle

class Assignment_ans(models.Model):
    student=models.ForeignKey(Stud, null=True, on_delete=models.SET_NULL)
    tittle=models.CharField(max_length=200, null=False)
    teacher=models.ForeignKey(Tutor, null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True, null =True)
    description = models.TextField(default='this id your lecture, document type lecture')

    def __str__(self):
        return self.tittle








