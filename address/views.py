from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .models import *


# Create your views here.
def country(request):
    country_list = Country.objects.all()
    template = loader.get_template('country_list.html')
    context = {
        'country_list': country_list
    }
    return HttpResponse(template.render(context, request))


def add_country(request):
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        phone_code = request.POST['phone_code']
        all_country = Country(name=name, code=code, phone_code=phone_code)
        all_country.save()
        return redirect('/country')
    return render(request, 'add_country.html')


def view_country(request, country_id):
    all_country = Country.objects.get(id=country_id)
    template = loader.get_template('view_country.html')
    context = {
        'all_country': all_country,
    }
    return HttpResponse(template.render(context, request))


def update_country(request, country_id):
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        phone_code = request.POST['phone_code']
        get_country_id = Country.objects.get(id=country_id)
        get_country_id.name = name
        get_country_id.code = code
        get_country_id.phone_code = phone_code
        get_country_id.save()
        return redirect('/country')
    return render(request, 'view_country.html')


def states(request):
    state_list = State.objects.all()
    template = loader.get_template('states.html')
    context = {
        'state_list': state_list
    }
    return HttpResponse(template.render(context, request))


def add_state(request):
    country_list = Country.objects.all()
    context = {
        'country_list': country_list
    }
    if request.method == "POST":
        name = request.POST['name']
        code = request.POST['code']
        country_id = request.POST['country_id']
        all_country = State(name=name, code=code, country_id=country_id)
        all_country.save()
        return redirect('/states')
    return render(request, 'add_state.html', context)


def city(request):
    city_list = City.objects.all()
    template = loader.get_template('city_list.html')
    context = {
        'city_list': city_list
    }
    return HttpResponse(template.render(context, request))


def add_city(request):
    country_list = Country.objects.all()
    state_list = State.objects.all()
    # state_list = State.objects.all().filter(country=)
    context = {
        'country_list': country_list,
        'state_list': state_list
    }
    if request.method == "POST":
        name = request.POST['name']
        zipcode = request.POST['zipcode']
        country_id = request.POST['country_id']
        state_id = request.POST['state_id']
        all_city = City(name=name, zipcode=zipcode, country_id=country_id, state_id=state_id)
        all_city.save()
        return redirect('/city')
    return render(request, 'add_city.html', context)
