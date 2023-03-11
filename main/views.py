from django.shortcuts import render
from .models import Banner
# Create your views here.

def index(request):
    sliders = Banner.objects.filter(state='sld')
    sub_banner = Banner.objects.filter(state='sub')
    single_banner = Banner.objects.filter(state='sng')
    small_banner = Banner.objects.filter(state='sml')

    context = {'sliders': sliders,
               'sub_banner': sub_banner,
               'single_banner': single_banner,
               'small_banner': small_banner}

    return render(request, 'main/index.html', context)



