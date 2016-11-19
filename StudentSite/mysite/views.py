from django.shortcuts import render, render_to_response, redirect
from mysite.models import Help_materials
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    return render(request, 'home.html', {'username': username})

def all_materials(request):
    return render_to_response('materials.html', {'materials': Help_materials.objects.all(), 'user_name': auth.get_user(request).username} )

def material_by_id(request, material_id):
     if Help_materials.objects.get(id=int(material_id)):
        return render_to_response('material.html', {'material': Help_materials.objects.get(id=int(material_id))})
     else:
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
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        new_userform = UserCreationForm(request.POST)
        if new_userform.is_valid():
            new_userform.save()
            newuser = authenticate(username=new_userform.cleaned_data['username'], password=new_userform.cleaned_data['password'])
            auth.login(request, newuser)
            return HttpResponseRedirect("/")
        else:
            args['form'] = new_userform
            # return render_to_response('registration.html', args)
            # return render_to_response('registration.html', context_instance=RequestContext(request))
            return
            render(request, "registration.html", {
                'form': form,
            })


