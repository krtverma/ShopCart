from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import login

urlpatterns=[
    url('',views.home),
    url('login/',login, {'template_name': 'login.html'}),
]


