from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.core.files.storage import FileSystemStorage

from .models import Module

def index(request):
    explainable_modules = Module.objects.all()
    context = {
        'modules' : explainable_modules
    }
    return render(request, 'explainable/index.html', context)

def module(request, route):
    module = get_object_or_404(Module, module_route=route)
    if request.method == 'POST' and request.FILES['data']:
        data = request.FILES['data']
        fs = FileSystemStorage()
        filename = fs.save(data.name, data)
        uploaded_file_url = fs.url(filename)
        return render(request, 'explainable/' + route + '.html', {"module" : module, "uploaded_file_url": uploaded_file_url})
    else:
        return render(request, 'explainable/' + route + '.html', {"module" : module})
