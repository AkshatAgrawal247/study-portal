from django.contrib import admin

from .models  import *

admin.site.register(Tutor)
admin.site.register(Exam)
admin.site.register(Assignment_ques)
admin.site.register(Assignment_ans)