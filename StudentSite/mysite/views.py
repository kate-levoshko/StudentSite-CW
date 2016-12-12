from django.shortcuts import render, render_to_response, redirect
from mysite.models import Help_materials
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout

from django.http import HttpResponseRedirect
from django.http import HttpResponse
import  json
from django.contrib.auth.models import User

import sys

def home (request):
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    return render(request, 'home.html', {'username': username})

def about( request):
    return render(request, 'about.html')

def all_materials(request):
        return render_to_response('materials.html', {'materials': Help_materials.objects.all(), 'user_name': auth.get_user(request).username} )

def material_by_id(request, material_id):
     try:
         return render_to_response('material.html', {'material': Help_materials.objects.get(id=int(material_id))})
     except:
        render_to_response('404.html', context_instance=RequestContext(request))


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
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            return render_to_response('login.html', {'error': 'We have a user with such name'})
        else:
            user = User.objects.create_user(request.POST['username'], request.POST['password'])

            user.save()
            custom_user = User.objects.create(User=user)
            custom_user.save()
    else:
        return render_to_response('registration.html', {})


