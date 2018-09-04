from django.shortcuts import render
from .models import SampleModel
# Create your views here.

def index(request):
    """SampleApp home page"""
    return render(request, 'SampleApp/index.html')

def sampleObjects(request):
    sampleObjects = SampleModel.objects.order_by('date_added')
    context = {'sampleObjects': sampleObjects}
    return render(request, 'SampleApp/sampleObjects.html', context)

def sampleObject(request, sampleObject_id):
    sampleObject = SampleModel.objects.get(id=sampleObject_id)
    entries = sampleObject.entry_set.order_by('-date_added')
    context = {'sampleObject': sampleObject, 'entries': entries}
    return render(request, 'SampleApp/sampleObject.html', context)
