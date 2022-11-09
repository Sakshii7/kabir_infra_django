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
    country_list = Country.objects.all()
    context = {
        'country_list': country_list,
    }
    if request.method == 'POST':
        name = request.POST['name']
        street = request.POST['street']
        street2 = request.POST['street2']
        city_id = request.POST['city_id']
        country_id = request.POST['country_id']
        state_id = request.POST['state_id']
        pincode = request.POST['pincode']
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        email = request.POST['email']
        all_clients = Clients(name=name, street=street, street2=street2, city_id=city_id, country_id=country_id, state_id=state_id,
                              pincode=pincode, phone=phone, mobile=mobile, email=email)
        all_clients.save()
        return redirect('/clients')
    return render(request, 'add_clients.html', context)


def load_states(request):
    country_id = request.GET.get('country')
    state = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'states_dropdown.html', {'state_list': state})


def load_city(request):
    state_id = request.GET.get('state')
    city = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'city_dropdown.html', {'city_list': city})


def view_clients(request, client_id):
    particular_client_id = Clients.objects.get(id=client_id)
    country_list = Country.objects.all()
    country = Clients.objects.filter(id=client_id).values_list('country_id', flat=True)
    state_list = State.objects.filter(country_id=country[0]).order_by('name')
    state = Clients.objects.filter(id=client_id).values_list('state_id', flat=True)
    city_list = City.objects.filter(state_id=state[0]).order_by('name')
    template = loader.get_template('view_clients.html')
    context = {
        'particular_client_id': particular_client_id,
        'country_list': country_list,
        'state_list': state_list,
        'city_list': city_list
    }
    return HttpResponse(template.render(context, request))


def update_clients(request, client_id):
    if request.method == 'POST':
        name = request.POST['name']
        street = request.POST['street']
        street2 = request.POST['street2']
        city_id = request.POST['city_id']
        country_id = request.POST['country_id']
        state_id = request.POST['state_id']
        pincode = request.POST['pincode']
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        email = request.POST['email']
        get_client_id = Clients.objects.get(id=client_id)
        get_client_id.name = name
        get_client_id.street = street
        get_client_id.street2 = street2
        get_client_id.city_id = city_id
        get_client_id.country_id = country_id
        get_client_id.state_id = state_id
        get_client_id.pincode = pincode
        get_client_id.phone = phone
        get_client_id.mobile = mobile
        get_client_id.email = email
        get_client_id.save()
        return redirect('/clients')
    return render(request, 'view_clients.html')
