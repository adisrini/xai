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
    obs = [[5.1, 2.8, 3, 0.4]]
    X, Y, plotData, chartLayout = plotmaker.makeIris(obs)

    model = ExplainableLinearSVC()
    model.fit(X, Y)
    explanation = model.explain(obs)

    hyperplaneData = plotmaker.hyperplane(model.coefs(), [0, 1, 2])
    flippedData = plotmaker.flip(explanation, obs)

    chartData = plotData + hyperplaneData + flippedData

    myChart = plotly.offline.plot({"data": chartData,
                                   "layout": chartLayout},
                                   output_type = "div",
                                   show_link = "False",
                                   include_plotlyjs = "False",
                                   link_text="")
    return render(request, 'explainable/example.html', {'features' : explanation.features(), 'confidence' : explanation.confidence(), 'chart' : myChart})

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
