from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
             return redirect('/thome/')
        else:
            return view_fun(request, *args,**kwargs)
    return wrapper_fun

def allowed_users(allowed_roles=[]):
    def decorator(view_fun):
        def wrapper_fun(request, *args,**kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_fun(request,*args,**kwargs)
            else:
                return HttpResponse('you are not authorized to view this page')
        return wrapper_fun
    return decorator

def teacher(view_fun):
    def wrapper_fun(request, *args,**kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'teacher':
            return view_fun(request,*args,**kwargs)
        if group== 'student':
            return redirect('/shome')
        else:
            return HttpResponse('you are not student nor teacher, to view this page')
    return wrapper_fun
