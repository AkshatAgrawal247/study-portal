from django.forms import ModelForm
from .models import *


class StudentProfileForm(ModelForm):

    class Meta:
        model = Stud
        fields=['name','phone','email']