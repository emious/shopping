from django.urls import path
from main import views
from shoping import settings

urlpatterns = [
    path('', views.index, name='index'),


]
