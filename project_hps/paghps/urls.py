from django import views
from django.urls import path
from paghps import views

urlpatterns = [
    path('', views.index, name='index')
]