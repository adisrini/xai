from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Module

def index(request):
    explainable_modules = Module.objects.all()
    context = {
        'modules' : explainable_modules
    }
    return render(request, 'explainable/index.html', context)

def flip(request):
    module = get_object_or_404(Module, module_route='flip')
    return render(request, 'explainable/flip.html', {"module" : module})
