from django.shortcuts import render

# Create your views here.

def index(request):
    """SampleApp home page"""
    return render(request, 'SampleApp/index.html')
