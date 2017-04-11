from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
import random
import numpy as np
import plotly
import plotly.graph_objs as go
from .models import Module, Dataset, OverwriteStorage, ExplainableModel
from .backend.models.x_linearsvc import ExplainableLinearSVC
from .backend.utils.datasets import Datasets
from .backend.view import plotmaker

def index(request):
    explainable_modules = Module.objects.all()
    context = {
        'modules' : explainable_modules
    }
    return render(request, 'explainable/index.html', context)

def example(request):
    X, Y, plotData, plotLayout = plotmaker.makeIris()

    model = ExplainableLinearSVC()

    model.fit(X, Y)

    myChart = plotly.offline.plot({"data": plotData,
                                   "layout": plotLayout},
                                   output_type = "div",
                                   show_link = "False",
                                   include_plotlyjs = "False",
                                   link_text="")
    return render(request, 'explainable/example.html', {'chart' : myChart})#, {'features' : explanation.features(), 'confidence' : explanation.confidence()})#, 'chart' : myChart})

def module(request, route):
    module = get_object_or_404(Module, module_route=route)
    if request.method == 'POST' and request.FILES['data']:
        data = request.FILES['data']
        fs = OverwriteStorage()
        filename = fs.save(data.name, data)
        uploaded_file_url = fs.url(filename)
        if len(Dataset.objects.filter(dataset_url = uploaded_file_url)) == 0:    # if non-existent, then save to database
            dataObject = Dataset(dataset_url = uploaded_file_url)
            dataObject.save()
        return render(request, 'explainable/' + route + '.html', {"module": module, "uploaded_file_url": uploaded_file_url, "models": ExplainableModel.objects.all()})
    else:
        return render(request, 'explainable/' + route + '.html', {"module" : module})
