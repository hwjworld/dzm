import sys, traceback
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse


def init_users(request):
    # User.objects.create_user('hwj', 'hwj@j.com', 'hwj123456')
    User.objects.create_user('ty', 'ty@j.com', 'ty123456')
    return HttpResponse('suc')

def login_ajax(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
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
