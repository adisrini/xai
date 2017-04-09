from django.shortcuts import render
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
    return HttpResponse("You're looking at the flip module.")
