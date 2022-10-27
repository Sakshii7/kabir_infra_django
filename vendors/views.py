from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

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
    if request.method == "POST":
        vendor_code = request.POST['vendor_code']
        trade_name = request.POST['trade_name']
        vendor_name = request.POST['vendor_name']
        street = request.POST['street']
        street2 = request.POST['street2']
        city = request.POST['city']
        country = request.POST['country']
        state = request.POST['state']
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
                              street2=street2, city=city, country=country, state=state, pincode=pincode, phone=phone,
                              mobile=mobile, email=email, gstin=gstin, pan_no=pan_no, vendor_type=vendor_type,
                              contact_person=contact_person, credit_days=credit_days, credit_amount=credit_amount)
        all_vendors.save()
        return redirect('/vendors')
    return render(request, 'add_vendors.html')
