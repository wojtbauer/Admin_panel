"""Defines url patterns for SampleApp."""

from django.urls import path
from . import views


app_name = 'SampleApp'
urlpatterns = [
    #Home page.
    path('', views.index, name='index'),
    
    #Show all sample objects.
    path('sampleObjects/', views.sampleObjects, name='sampleObjects'),
    
    #Detail page for a single object.
    path('sampleObjects/<int:sampleObject_id>/', views.sampleObject, 
    name='sampleObject'),

    #Page for adding a new sampleObject.
    path('new_sampleObject/', views.new_sampleObject, name='new_sampleObject'),

    #Page for adding a new entry.
    path('new_entry/<int:sampleObject_id>/', views.new_entry, name='new_entry'),

    #Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
 
]
