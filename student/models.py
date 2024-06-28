from django.db import models
from django.contrib.auth.models import User

class Stud(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True,default='test student')
    phone=models.CharField(max_length=200, null=True,default='1234')
    email= models.CharField(max_length=200, null=True,default='name@mail')

    def __str__(self):
        return self.name

