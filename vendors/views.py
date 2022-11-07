from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from address.models import City
from .models import *


# Create your views here.

def vendors(request):
    vendor_list = Vendors.objects.all()
    template = loader.get_template('vendors.html')
    context = {
        'vendor_list': vendor_list
    }
    return HttpResponse(template.render(context, request))


def add_vendors(request):
    country_list = Country.objects.all()
    context = {
        'country_list': country_list,
    }
    if request.method == "POST":
        vendor_code = request.POST['vendor_code']
        trade_name = request.POST['trade_name']
        vendor_name = request.POST['vendor_name']
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
        vendor_type = request.POST['vendor_type']
        contact_person = request.POST['contact_person']
        credit_days = request.POST['credit_days']
        credit_amount = request.POST['credit_amount']
        all_vendors = Vendors(vendor_code=vendor_code, trade_name=trade_name, vendor_name=vendor_name, street=street,
                              street2=street2, city_id=city_id, country_id=country_id, state_id=state_id,
                              pincode=pincode, phone=phone,
                              mobile=mobile, email=email, gstin=gstin, pan_no=pan_no, vendor_type=vendor_type,
                              contact_person=contact_person, credit_days=credit_days, credit_amount=credit_amount)
        all_vendors.save()
        return redirect('/vendors')
    return render(request, 'add_vendors.html', context)


def load_states(request):
    country_id = request.GET.get('country')
    state = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'states_dropdown.html', {'state_list': state})


def load_city(request):
    state_id = request.GET.get('state')
    city = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'city_dropdown.html', {'city_list': city})

