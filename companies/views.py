from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .models import *


# Create your views here.

def companies(request):
    company_list = Company.objects.all()
    template = loader.get_template('companies.html')
    context = {
        'company_list': company_list
    }
    return HttpResponse(template.render(context, request))


def add_company(request):
    country_list = Country.objects.all()
    context = {
        'country_list': country_list,
    }
    if request.method == "POST":
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
        gstin = request.POST['gstin']
        pan_no = request.POST['pan_no']
        cin_no = request.POST['cin_no']
        company_registry = request.POST['company_registry']
        owner_name = request.POST['owner_name']
        currency = request.POST['currency']
        company_id = Company(name=name, street=street,
                             street2=street2, city_id=city_id, country_id=country_id, state_id=state_id,
                             pincode=pincode, phone=phone,
                             mobile=mobile, email=email, gstin=gstin, pan_no=pan_no, cin_no=cin_no,
                             company_registry=company_registry, owner_name=owner_name, currency=currency)
        company_id.save()
        return redirect('/companies')
    return render(request, 'add_company.html', context)


def load_states(request):
    country_id = request.GET.get('country')
    state = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'states_dropdown.html', {'state_list': state})


def load_city(request):
    state_id = request.GET.get('state')
    city = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'city_dropdown.html', {'city_list': city})
