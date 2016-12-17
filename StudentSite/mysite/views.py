from django.shortcuts import render, render_to_response, redirect
from mysite.models import Help_materials
from django.template import RequestContext
from django.contrib import auth
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as dj_login
# from django.contrib.auth import logout as dj_logout
from . import forms
from StudentSite import settings

from django.http import HttpResponseRedirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
# import sys

import json, os

def home (request):
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    return render(request, 'home.html', {'username': username})

def about(request):
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    return render(request, 'about.html', {'username': username})

def contacts(request):
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    return render(request, 'contacts.html', {'username': username})

def account(request):
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    return render(request, 'account.html', {'username': username})

def all_materials(request):
    if request.method == "POST":
        form = forms.upload_file_form(request.POST, request.FILES)
        if form.is_valid():
            #uplouded_file(request.FILES['material'])
            Help_materials.objects.create(upload_material=request.FILES['material'],
                                            faculty=request.POST['faculty'],
                                            year_discipline=int(request.POST['year']),
                                            professor=request.POST['professor'],
                                            discipline=request.POST['discipline'])
        else:
            print("Form is invalid")
    print( Help_materials.objects.all())
    return render(request, 'materials.html', {'materials': Help_materials.objects.all(),  "user": request.user} )


def material_by_id(request, material_id):
     try:
         username = request.user.username
         return render(request, 'material.html', {'material': Help_materials.objects.get(id=int(material_id)), 'username': username })
     except:
        username = None
        render(request, '404.html', context_instance=RequestContext(request))


def uplouded_file(f):
    with open(os.path.join(settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def bucket(request):
    args = {}
    if request.method == "GET":
        args['user'] = request.user
        args['materials'] = request.user.my_material.all()
        return render(request, 'materials.html', args)
    elif request.method == "POST":
        request.POST['add']
    elif request.method == "DELETE":
        try:
            Help_materials.users.though.objects.get(user_id=int(request.GET['user']), material_id=request.material.id).delete()
        except:
            return HttpResponse(json.dumps({"status": "error"}), content_type="application/json")
            return HttpResponse(json.dumps({"status": "ok"}), content_type="application/json")


def search(request):
    materials_fac = Help_materials.objects.none()
    flag = True
    if 'search' in request.GET:
        search = request.GET['search'].split()
        for val in search:
            if flag:
                new_materials = Help_materials.objects.filter(faculty__icontains=val)
                if new_materials:
                    materials_fac = new_materials
                else:
                    continue
                flag = False
            else:
                new_materials = materials_fac & Help_materials.objects.filter(faculty__icontains=val)
                if new_materials:
                    materials_fac = new_materials
    materials_prof = Help_materials.objects.none()
    flag = True
    if 'search' in request.GET:
        search = request.GET['search'].split()
        for val in search:
            if flag:
                new_materials = Help_materials.objects.filter(professor__icontains=val)
                if new_materials:
                    materials_prof = new_materials
                else:
                    continue
                flag = False
            else:
                new_materials = materials_prof & Help_materials.objects.filter(professor__icontains=val)
                if new_materials:
                    materials_prof = new_materials
    materials_dis = Help_materials.objects.none()
    flag = True
    if 'search' in request.GET:
        search = request.GET['search'].split()
        for val in search:
            if flag:
                new_materials = Help_materials.objects.filter(discipline__icontains=val)
                if new_materials:
                    materials_dis = new_materials
                else:
                    continue
                flag = False
            else:
                new_materials = materials_dis & Help_materials.objects.filter(discipline__icontains=val)
                if new_materials:
                    materials_dis = new_materials
    materials_year = Help_materials.objects.none()
    flag = True
    if 'search' in request.GET:
        search = request.GET['search'].split()
        for val in search:
            if flag:
                new_materials = Help_materials.objects.filter(year_discipline__icontains=val)
                if new_materials:
                    materials_year = new_materials
                else:
                    continue
                flag = False
            else:
                new_materials = materials_year & Help_materials.objects.filter(year_discipline__icontains=val)
                if new_materials:
                    materials_year = new_materials
    materials_file = Help_materials.objects.none()
    flag = True
    if 'search' in request.GET:
        search = request.GET['search'].split()
        for val in search:
            if flag:
                new_materials = Help_materials.objects.filter(upload_material__icontains=val)
                if new_materials:
                    materials_file = new_materials
                else:
                    continue
                flag = False
            else:
                new_materials = materials_file & Help_materials.objects.filter(upload_material__icontains=val)
                if new_materials:
                    materials_file = new_materials
    materials = materials_fac | materials_dis | materials_prof | materials_year | materials_file
    return HttpResponse(json.dumps([i.dict() for i in materials]), content_type='application/javascript')