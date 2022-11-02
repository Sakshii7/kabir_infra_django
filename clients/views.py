from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

# Create your views here.
from .models import *


def clients(request):
    client_list = Clients.objects.all()
    template = loader.get_template('clients.html')
    context = {
        'client_list': client_list
    }
    return HttpResponse(template.render(context, request))


def add_clients(request):
    if request.method == 'POST':
        name = request.POST['name']
        street = request.POST['street']
        street2 = request.POST['street2']
        city = request.POST['city']
        country = request.POST['country']
        state = request.POST['state']
        pincode = request.POST['pincode']
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        email = request.POST['email']
        all_clients = Clients(name=name, street=street, street2=street2, city=city, country=country, state=state,
                              pincode=pincode, phone=phone, mobile=mobile, email=email)
        all_clients.save()
        return redirect('/clients')
    return render(request, 'add_clients.html')


def view_clients(request, client_id):
    all_clients = Clients.objects.get(id=client_id)
    template = loader.get_template('view_clients.html')
    context = {
        'all_clients': all_clients,
    }
    return HttpResponse(template.render(context, request))


def update_clients(request, client_id):
    if request.method == 'POST':
        name = request.POST['name']
        street = request.POST['street']
        street2 = request.POST['street2']
        city = request.POST['city']
        country = request.POST['country']
        state = request.POST['state']
        pincode = request.POST['pincode']
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        email = request.POST['email']
        get_client_id = Clients.objects.get(id=client_id)
        get_client_id.name = name
        get_client_id.street = street
        get_client_id.street2 = street2
        get_client_id.city = city
        get_client_id.country = country
        get_client_id.state = state
        get_client_id.pincode = pincode
        get_client_id.phone = phone
        get_client_id.mobile = mobile
        get_client_id.email = email
        get_client_id.save()
        return redirect('/clients')
    return render(request, 'view_clients.html')
