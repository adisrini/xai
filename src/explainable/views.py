from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    explainable_modules = {'flip': 'Quantify the robustness of a model when presented a new observation.'}
    template = loader.get_template('explainable/index.html')
    context = {
        'options' : explainable_modules
    }
    return HttpResponse(template.render(context, request))

def flip(request):
    return HttpResponse("You're looking at the flip module.")
