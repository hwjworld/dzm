import sys, traceback
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.views import redirect_to_login
from django.views.decorators.csrf import csrf_exempt, csrf_protect,ensure_csrf_cookie
from django.http import HttpResponse


def init_users(request):
    # User.objects.create_user('hwj', 'hwj@j.com', 'hwj123456')
    User.objects.create_user('ty', 'ty@j.com', 'ty123456')
    return HttpResponse('suc')

@login_required
@ensure_csrf_cookie
@csrf_exempt
def users(request):
    users = User.objects.all()
    return render_to_response('volunteers/users.html',{'volunteers':users})

@csrf_exempt
@ensure_csrf_cookie
@login_required
def user_add(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username, email,password)
    users = User.objects.all()
    return render_to_response('volunteers/users.html',{'volunteers':users})


def login_ajax(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            request.session.set_expiry(18000)
            return redirect('/menu')

        else:
            return redirect_to_login('/menu')
            # return("disabled account")
            # Return a 'disabled account' error message
    else:
        return redirect_to_login('/menu')
        # return render_to_response('/login/')
        # return ("invalid login")
        # Return an 'invalid login' error message.
