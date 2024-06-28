from django import forms
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    group=forms.ChoiceField(choices=(('student','student'),('teacher','teacher')))

    class Meta:
        model=User
        fields = ['username','email','password1','password2']
