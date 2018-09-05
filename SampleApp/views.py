from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import SampleModel
from .forms import SampleModelForm
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

def new_sampleObject(request):
    if request.method != "POST":
        form = SampleModelForm()
    else:
        form = SampleModelForm(request.POST)
        if form.is_valid():
            new_sampleObject = form.save(commit=False)
            new_sampleObject.owner = request.user
            new_sampleObject.save()
            return HttpResponseRedirect(reverse('SampleApp:sampleObjects'))        
            
    context = {'form': form}
    return render(request, 'SampleApp/new_sampleObject.html', context)
