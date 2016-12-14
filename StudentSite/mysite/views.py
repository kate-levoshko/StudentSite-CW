from django.shortcuts import render, render_to_response, redirect
from mysite.models import Help_materials
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from . import forms
from StudentSite import settings

from django.http import HttpResponseRedirect
from django.http import HttpResponse
import  json, os

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
    if request.method == "POST":
        form = forms.upload_file_form(request.POST, request.FILES)
        if form.is_valid():
            uplouded_file(request.FILES['material'])
            Help_materials.objects.create(upload_material = request.FILES['material'],
                                            faculty = request.POST['faculty'],
                                            year_discipline=int(request.POST['year']),
                                            professor=request.POST['professor'],
                                            discipline=request.POST['discipline'])
        else:
            print("Form is invalid")
    return render_to_response('materials.html', {'materials': Help_materials.objects.all(), 'user_name': auth.get_user(request).username, "user": request.user.is_authenticated} )



def material_by_id(request, material_id):
     try:
         return render_to_response('material.html', {'material': Help_materials.objects.get(id=int(material_id))})
     except:
        render_to_response('404.html', context_instance=RequestContext(request))


def uplouded_file(f):
    with open(os.path.join(settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
