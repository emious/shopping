import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.forms import ProfileRegisterForm
from account.models import ProfileModel, provincesModel, citiesModel
from shoping import settings
from main.views import index
from django.contrib.auth.models import User


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('login-pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                'username': username,
                'errorMessage': 'کاربر مورد نظر یافت نشد'
            }
            return render(request, 'account/login.html', context)
    else:
        return render(request, 'account/login.html', {})


def register_page(request):
    if request.method == "POST":
        profile_register_form = ProfileRegisterForm(request.POST, request.FILES)

        if username_exists(request.POST.get('username')):
            context = {
                'username': request.POST.get('username'),
                'errorMessage': 'نام کاربری مورد نظر تکراری می‌باشد'
            }
            return render(request, 'account/register.html', context)
        else:
            if profile_register_form.is_valid():
                user = User.objects.create_user(username=profile_register_form.cleaned_data["username"],
                                                email=profile_register_form.cleaned_data['email'],
                                                password=profile_register_form.cleaned_data['password'],
                                                first_name=profile_register_form.cleaned_data['f_name'],
                                                last_name=profile_register_form.cleaned_data['l_name'])
                user.save()

                profileModel = ProfileModel(user=user,
                                            mobile=profile_register_form.cleaned_data['mobile'])
                profileModel.save()
                return HttpResponseRedirect(reverse(index))
    return render(request, 'account/register.html')


@login_required
def info_page(request):
    profile = ProfileModel.objects.get(user=request.user)
    context = {"profile": profile,
               'cities': citiesModel.objects.filter(province_id=30),
               'provinces': provincesModel.objects.all}
    #return HttpResponse(profile.user.email)

    return render(request, 'account/account.html', context)


def username_exists(username):
    if User.objects.filter(username=username).exists():
        return True
    return False


@api_view(['POST'])
def get_cities_base_on_province(request):
    if request.method == 'POST':
        province_id = request.data['id']
        city_object_list = citiesModel.objects.filter(province_id=province_id)
        cities_list = [x.name for x in city_object_list]
        return Response(cities_list)


