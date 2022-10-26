from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import *


# Create your views here.
def view_materials(request):
    material_list = Materials.objects.all()
    template = loader.get_template('materials.html')
    context = {
        'material_list': material_list
    }
    return HttpResponse(template.render(context, request))


def add_materials(request):
    if request.method == 'POST':
        material_code = request.POST['material_code']
        name = request.POST['name']
        alias_name = request.POST['alias_name']
        quantity = request.POST['quantity']
        conversion_quantity = request.POST['conversion_quantity']
        gst_rate = request.POST['gst_rate']
        allowable_tolerance = request.POST['allowable_tolerance']
        materials = Materials(material_code=material_code, name=name, alias_name=alias_name,
                              quantity=quantity, conversion_quantity=conversion_quantity, gst_rate=gst_rate,
                              allowable_tolerance=allowable_tolerance)
        materials.save()
        return redirect('/materials/view_materials')
    return render(request, 'add_materials.html')
