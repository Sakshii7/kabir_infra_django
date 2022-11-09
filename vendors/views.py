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


def view_vendor(request, vendor_id):
    particular_vendor_id = Vendors.objects.get(id=vendor_id)
    country_list = Country.objects.all()
    country = Vendors.objects.filter(id=vendor_id).values_list('country_id', flat=True)
    state_list = State.objects.filter(country_id=country[0]).order_by('name')
    state = Vendors.objects.filter(id=vendor_id).values_list('state_id', flat=True)
    city_list = City.objects.filter(state_id=state[0]).order_by('name')
    template = loader.get_template('view_vendor.html')
    context = {
        'particular_vendor_id': particular_vendor_id,
        'country_list': country_list,
        'state_list': state_list,
        'city_list': city_list
    }
    return HttpResponse(template.render(context, request))


def update_vendor(request, vendor_id):
    if request.method == 'POST':
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
        get_vendor_id = Vendors.objects.get(id=vendor_id)
        get_vendor_id.vendor_code = vendor_code
        get_vendor_id.trade_name = trade_name
        get_vendor_id.vendor_name = vendor_name
        get_vendor_id.street = street
        get_vendor_id.street2 = street2
        get_vendor_id.city_id = city_id
        get_vendor_id.country_id = country_id
        get_vendor_id.state_id = state_id
        get_vendor_id.pincode = pincode
        get_vendor_id.phone = phone
        get_vendor_id.mobile = mobile
        get_vendor_id.email = email
        get_vendor_id.gstin = gstin
        get_vendor_id.pan_no = pan_no
        get_vendor_id.vendor_type = vendor_type
        get_vendor_id.contact_person = contact_person
        get_vendor_id.credit_days = credit_days
        get_vendor_id.credit_amount = credit_amount
        get_vendor_id.save()
        return redirect('/vendors')
    return render(request, 'view_vendor.html')
