# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .models import *


def sites(request):
    site_list = Sites.objects.all()
    template = loader.get_template('sites.html')
    context = {
        'site_list': site_list
    }
    return HttpResponse(template.render(context, request))


def add_sites(request):
    client_list = Clients.objects.all()
    country_list = Country.objects.all()
    context = {
        'client_list': client_list,
        'country_list': country_list
    }
    if request.method == "POST":
        site_no = request.POST['site_no']
        site_desc = request.POST['site_desc']
        alias_name = request.POST['alias_name']
        street = request.POST['street']
        street2 = request.POST['street2']
        city_id = request.POST['city']
        country_id = request.POST['country']
        state_id = request.POST['state']
        pincode = request.POST['pincode']
        client_id = request.POST['client_id']
        company = request.POST['company']

        all_sites = Sites(site_no=site_no, site_desc=site_desc, alias_name=alias_name, street=street, street2=street2,
                          city_id=city_id, country_id=country_id, state_id=state_id, pincode=pincode,
                          client_id=client_id,
                          company=company)
        all_sites.save()
        return redirect('/sites')
    return render(request, 'add_sites.html', context)


def load_states(request):
    country_id = request.GET.get('country')
    state = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'states_dropdown.html', {'state_list': state})


def load_city(request):
    state_id = request.GET.get('state')
    city = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'city_dropdown.html', {'city_list': city})


def view_sites(request, site_id):
    all_sites = Sites.objects.get(id=site_id)
    template = loader.get_template('view_sites.html')
    client_list = Clients.objects.all()
    context = {
        'all_sites': all_sites,
        'client_list': client_list
    }
    return HttpResponse(template.render(context, request))


def update_sites(request, site_id):
    client_list = Clients.objects.all()
    context = {
        'client_list': client_list
    }
    if request.method == 'POST':
        site_no = request.POST['site_no']
        site_desc = request.POST['site_desc']
        alias_name = request.POST['alias_name']
        street = request.POST['street']
        street2 = request.POST['street2']
        city = request.POST['city']
        country = request.POST['country']
        state = request.POST['state']
        pincode = request.POST['pincode']
        client_id = request.POST['client_id']
        company = request.POST['company']
        match_site_id = Sites.objects.get(id=site_id)
        match_site_id.site_no = site_no
        match_site_id.site_desc = site_desc
        match_site_id.alias_name = alias_name
        match_site_id.street = street
        match_site_id.street2 = street2
        match_site_id.city = city
        match_site_id.country = country
        match_site_id.state = state
        match_site_id.pincode = pincode
        match_site_id.client_id = client_id
        match_site_id.company = company
        match_site_id.save()
        return redirect('/sites')
    return render(request, 'view_clients.html', context)
