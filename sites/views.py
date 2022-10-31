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
    client_list = Clients.objects.get()
    context = {
        'client_list': client_list
    }
    if request.method == "POST":
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

        all_sites = Sites(site_no=site_no, site_desc=site_desc, alias_name=alias_name, street=street, street2=street2,
                          city=city, country=country, state=state, pincode=pincode, client_id=client_id, company=company)
        all_sites.save()
        return redirect('/sites')
    return render(request, 'add_sites.html', context)
