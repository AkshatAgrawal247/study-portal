from django.forms import ModelForm
from .models import *

class ExamForm(ModelForm):

    class Meta:
        model = Exam
        fields='__all__'


class ProfileForm(ModelForm):

    class Meta:
        model = Tutor
        fields=['name','phone','email']


class Assignment_ques_Form(ModelForm):

    class Meta:
        model = Assignment_ques
        fields='__all__'


class Assignment_ans_Form(ModelForm):

    class Meta:
        model = Assignment_ans
        fields='__all__'