"""Defines url patterns for SampleApp."""

from django.urls import path
from . import views


app_name = 'SampleApp'
urlpatterns = [
    #Home page.
    path('', views.index, name='index'),
    
    #Show all sample objects.
    path('sampleObjects/', views.sampleObjects, name='sampleObjects'),
    
    #Detail page for an single object.
    path('sampleObjects/<int:sampleObject_id>/', views.sampleObject, 
    name='sampleObject'),

    #Page for adding a new sampleObject.
    path('new_sampleObject/', views.new_sampleObject, name='new_sampleObject'),
]
