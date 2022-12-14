from sre_parse import State

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


def view_state(request, state_id):
    all_state = State.objects.get(id=state_id)
    country_list = Country.objects.all()
    template = loader.get_template('view_state.html')
    context = {
        'all_state': all_state,
        'country_list': country_list
    }
    return HttpResponse(template.render(context, request))


def update_state(request, state_id):
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        country_id = request.POST['country_id']
        get_state_id = State.objects.get(id=state_id)
        get_state_id.name = name
        get_state_id.code = code
        get_state_id.country_id = country_id
        get_state_id.save()
        return redirect('/states')
    return render(request, 'view_state.html')


def city(request):
    city_list = City.objects.all()
    template = loader.get_template('city_list.html')
    context = {
        'city_list': city_list
    }
    return HttpResponse(template.render(context, request))


def add_city(request):
    country_list = Country.objects.all()
    context = {
        'country_list': country_list,
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


def load_states(request):
    country_id = request.GET.get('country')
    state = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'states_dropdown.html', {'state_list': state})


def view_city(request, city_id):
    particular_city_id = City.objects.get(id=city_id)
    country_list = Country.objects.all()
    get_country_id = City.objects.filter(id=city_id).values_list('country_id', flat=True)
    state_list = State.objects.filter(country_id=get_country_id[0]).order_by('name')
    template = loader.get_template('view_city.html')
    context = {
        'particular_city_id': particular_city_id,
        'country_list': country_list,
        'state_list': state_list,
    }
    return HttpResponse(template.render(context, request))


def update_city(request, city_id):
    if request.method == 'POST':
        name = request.POST['name']
        zipcode = request.POST['zipcode']
        country_id = request.POST['country_id']
        state_id = request.POST['state_id']
        get_city_id = State.objects.get(id=city_id)
        get_city_id.name = name
        get_city_id.code = zipcode
        get_city_id.country_id = country_id
        get_city_id.state_id = state_id
        get_city_id.save()
        return redirect('/city')
    return render(request, 'view_city.html')
