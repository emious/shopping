from django.urls import path
from account import views
from shoping import settings

urlpatterns = [
    path('login_page', views.login_page),
    path('register_page', views.register_page),
    path('info_page', views.info_page),
    path('get_cities_api', views.get_cities_base_on_province),

]
