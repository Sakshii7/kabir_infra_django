from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import *
from datetime import datetime


# Create your views here.

def materials(request):
    material_requisition = Materials.objects.all()
    template = loader.get_template('requisition.html')
    context = {
        'material_requisition': material_requisition
    }
    return HttpResponse(template.render(context, request))


def homepage(request):
    material_requisition = Materials.objects.all()
    template = loader.get_template('requisition.html')
    context = {
        'material_requisition': material_requisition
    }
    return HttpResponse(template.render(context, request))


def add_material_requisition(request):
    if request.method == 'POST':
        name = request.POST['name']
        site_id = request.POST['site_id']
        user_id = request.POST['user_id']
        d = datetime.now().date()
        requisition_date = d
        material_requisition = Materials(name=name, site_id=site_id, user_id=user_id, requisition_date=requisition_date)
        material_requisition.save()
        messages.info(request, 'Material Requisition Added.')
    return render(request, 'add_requisition.html')
