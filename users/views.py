from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from users.models import Users


# Create your views here.


def users(request):
    user_list = Users.objects.all()
    template = loader.get_template('users.html')
    context = {
        'user_list': user_list
    }
    return HttpResponse(template.render(context, request))


def add_user(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        is_supervisior = request.POST.get('is_supervisior', '') == 'on'
        is_accounts = request.POST.get('is_accounts', '') == 'on'
        is_purchase = request.POST.get('is_purchase', '') == 'on'
        is_administrator = request.POST.get('is_purchase', '') == 'on'
        is_add_sites_and_vendors = request.POST.get('is_purchase', '') == 'on'
        if is_supervisior:
            all_users = Users(name=name, email=email, is_supervisior=is_supervisior)
            all_users.save()
        elif is_accounts:
            all_users = Users(name=name, email=email, is_accounts=is_accounts)
            all_users.save()
        elif is_purchase:
            all_users = Users(name=name, email=email, is_purchase=is_purchase)
            all_users.save()
        elif is_administrator:
            all_users = Users(name=name, email=email, is_administrator=is_administrator)
            all_users.save()
        elif is_add_sites_and_vendors:
            all_users = Users(name=name, email=email, is_add_sites_and_vendors=is_add_sites_and_vendors)
            all_users.save()
        else:
            all_users = Users(name=name, email=email)
            all_users.save()
        return redirect('/users')
    return render(request, 'add_user.html')


def view_user(request, user_id):
    user = Users.objects.get(id=user_id)
    template = loader.get_template('view_user.html')
    context = {
        'user_list': user,
    }
    return HttpResponse(template.render(context, request))


def update_user(request, user_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        is_supervisior = request.POST.get('is_supervisior', '') == 'on'
        is_accounts = request.POST.get('is_accounts', '') == 'on'
        is_purchase = request.POST.get('is_purchase', '') == 'on'
        is_administrator = request.POST.get('is_purchase', '') == 'on'
        is_add_sites_and_vendors = request.POST.get('is_purchase', '') == 'on'
        particular_user_id = Users.objects.get(id=user_id)
        particular_user_id.name = name
        particular_user_id.email = email
        particular_user_id.is_supervisior = is_supervisior
        particular_user_id.is_accounts = is_accounts
        particular_user_id.is_purchase = is_purchase
        particular_user_id.is_administrator = is_administrator
        particular_user_id.is_add_sites_and_vendors = is_add_sites_and_vendors
        particular_user_id.save()
        return redirect('/users')
    return render(request, 'view_user.html')


def supervisiors(request):
    user_name = Users.objects.filter(is_supervisior=True).order_by('name')
    template = loader.get_template('supervisior.html')
    context = {
        'supervisior_list': user_name
    }
    return HttpResponse(template.render(context, request))
