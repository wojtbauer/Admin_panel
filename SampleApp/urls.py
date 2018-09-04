"""Defines url patterns for SampleApp."""

from django.urls import path
from . import views


app_name = 'SampleApp'
urlpatterns = [
    #Home page.
    path('', views.index, name='index'),
    
    #Show all sample objects.
    path('sampleObjects/', views.sampleObjects, name='sampleObjects'),
]
