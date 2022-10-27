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
