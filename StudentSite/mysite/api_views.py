from django.shortcuts import render, render_to_response, redirect
from mysite.models import Help_materials
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout

from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json
from django.contrib.auth.models import User

import sys

def all_materials(request):
    return HttpResponse(json.dumps([i.dict() for i in Help_materials.objects.all()]), content_type="application/json")

def material_by_id(request, material_id):
     try:
         return HttpResponse(json.dumps(Help_materials.objects.get(id=int(material_id)).dict()), content_type="application/json")
     except:
       return HttpResponse(json.dumps({'error': 'no material with such id'}))


