from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import *


# Create your views here.

def material_requisition(request):
    material_req = MaterialReq.objects.all()
    template = loader.get_template('requisition.html')
    context = {
        'material_req': material_req
    }
    return HttpResponse(template.render(context, request))


def add_material_requisition(request):
    if request.method == 'POST':
        name = request.POST['name']
        site_id = request.POST['site_id']
        user_id = request.POST['user_id']
        d = datetime.now().date()
        requisition_date = d
        material_req = MaterialReq(name=name, site_id=site_id, user_id=user_id, requisition_date=requisition_date)
        material_req.save()
        return redirect('/')
    return render(request, 'add_requisition.html')


def view_material_req(request, req_id):
    material_req = MaterialReq.objects.get(id=req_id)
    template = loader.get_template('view_requisition.html')
    context = {
        'material_req': material_req,
    }
    return HttpResponse(template.render(context, request))


def update_material_req(request, req_id):
    if request.method == 'POST':
        name = request.POST['name']
        site_id = request.POST['site_id']
        user_id = request.POST['user_id']
        requisition_id = MaterialReq.objects.get(id=req_id)
        requisition_id.name = name
        requisition_id.site_id = site_id
        requisition_id.user_id = user_id
        requisition_id.save()
        return redirect('/')
    return render(request, 'add_requisition.html')

# def pdf_view(request):
#     response = HttpResponse(content_type='application/pdf')
#
#     # This line force a download
#
#     response['Content-Disposition'] = 'attachment; filename="Custom Material Requisition.pdf"'
#
#     # READ Optional GET param
#     get_param = request.GET.get('x', 'World')
#
#     p = canvas.Canvas(response)
#
#     # Write content on the PDF
#     p.drawString(100, 500, "Hello " + get_param)
#
#     # Close the PDF object.
#     p.showPage()
#     p.save()
#
#     # Show the result to the user
#     return response
