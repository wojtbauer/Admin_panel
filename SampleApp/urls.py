"""Defines url patterns for SampleApp."""

from django.urls import path
from . import views


app_name = 'SampleApp'
urlpatterns = [
    #home page.
    path('', views.index, name='index'),
]
