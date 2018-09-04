from django.shortcuts import render
from .models import SampleModel
# Create your views here.

def index(request):
    """SampleApp home page"""
    return render(request, 'SampleApp/index.html')

def sampleObjects(request):
    sampleObjects = SampleModel.objects.ordered_by('date_added')
    context = {'sampleObjects': sampleObjects}
    return render(request, 'SampleApp/sampleObjects.html', context)
