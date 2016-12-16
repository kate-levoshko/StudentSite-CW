from django.shortcuts import render, render_to_response, redirect


from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.http import HttpResponse

import sys

def login(request):
    args = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                dj_login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User is not found"
            return render(request,'login.html', args)
    else:
        return render(request,'login.html', args)

def logout(request):
    dj_logout(request)
    return redirect('/')


def register(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST['username'])
            if user is not None:
                return render(request, 'registration.html', {'login_error': 'User with such name is already exists'})
        except:
            if request.POST['password'] == request.POST['password2']:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                                first_name=request.POST['name'], last_name=request.POST['surname'])
                user.save()
                return login(request)
            else:
                return render(request,'registration.html', {'pass_error': 'Passwords are not similar'})
    else:
        return render(request, 'registration.html', {})


