from django.shortcuts import render, render_to_response, redirect


from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.models import User

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
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    dj_logout(request)
    return redirect('/')


def register(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        password2=request.POST['password'])
        if user is not None:
            return render_to_response('registration.html', {'error': 'We have a user with such name'})
        # elif:
        #    //
        else:
            user = User.objects.create_user(request.POST['username'], request.POST['password'])

            user.save()
            custom_user = User.objects.create(User=user)
            custom_user.save()
    else:
        return render_to_response('registration.html', {})