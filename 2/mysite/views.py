from django.shortcuts import render, render_to_response
from mysite.models import Helper
from django.template import RequestContext

def home(request):
    return render(request, 'home.html')

def all_materials(request):
    return render_to_response('materials.html', {'materials':Helper.objects.all()})

def material_by_id(request, material_id):
    if (Helper.objects.get(id) == material_id):
        return render_to_response('material.html', {'material': Helper.objects.get(material_id)})
    else:
        render_to_response('404.html', context_instance=RequestContext(request))

