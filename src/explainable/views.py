from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.conf import settings
import random
import numpy as np
import plotly
import csv
import plotly.graph_objs as go
from .models import Module, Dataset, OverwriteStorage, ExplainableModel
from .backend.models.x_linearsvc import ExplainableLinearSVC
from .backend.models.x_linearsgdc import ExplainableSGDClassifier
from .backend.models.x_perceptron import ExplainablePerceptron
from .backend.utils.datasets import Datasets
from .backend.view import plotmaker
import ast

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

def flip(request, stage=1):
    module = get_object_or_404(Module, module_route='flip')
    stage = int(stage)
    if stage == 1:
        return render(request, 'explainable/flip.html', {"module" : module, "stage" : 1})
    elif stage == 2:
        data = request.FILES['data']
        fs = OverwriteStorage()
        filename = fs.save(data.name, data)
        uploaded_file_url = fs.url(filename)
        if len(Dataset.objects.filter(dataset_url = uploaded_file_url)) == 0:    # if non-existent, then save to database
            dataObject = Dataset(dataset_url = uploaded_file_url)
            dataObject.save()
        return render(request, 'explainable/flip.html', {"module": module, "stage" : 2, "uploaded_file_url" : uploaded_file_url, "models": ExplainableModel.objects.all()})
    elif stage == 3:
        selected_model = request.POST.get('selected_model', 'Linear Support Vector Classifier')
        uploaded_file_url = request.POST.get('uploaded_file_url', 'ERROR')
        header = []
        with open(settings.BASE_DIR + uploaded_file_url, 'rt') as f:
            reader = csv.reader(f, delimiter = ',', )
            header = next(reader)
        return render(request, 'explainable/flip.html', {"module" : module, "stage" : 3, "uploaded_file_url" : uploaded_file_url, "selected_model" : selected_model, "features" : range(1, len(header)), "num_features" : len(header)})
    elif stage == 4:
        selected_model = request.POST.get('selected_model', 'Linear Support Vector Classifier')
        uploaded_file_url = request.POST.get('uploaded_file_url', 'ERROR')
        num_features = int(request.POST.get('num_features', []))
        int_idxs = []
        str_idxs = []
        for i in range(1, num_features):
            res = request.POST.get(str(i), -1)
            if res == -1:
                str_idxs.append(i)
            else:
                int_idxs.append(i)
        return render(request, 'explainable/flip.html', {"module" : module, "stage" : 4, "uploaded_file_url" : uploaded_file_url, "selected_model" : selected_model, "int_idxs" : int_idxs, "str_idxs" : str_idxs})
    elif stage == 5:
        selected_model = request.POST.get('selected_model', 'Linear Support Vector Classifier')
        uploaded_file_url = request.POST.get('uploaded_file_url', 'ERROR')
        int_idxs = request.POST.get('int_idxs', [])
        str_idxs = request.POST.get('str_idxs', [])
        observation = request.POST.get('observation', "")
        obs = [ast.literal_eval('[' + observation + ']')]
        model = None
        if selected_model == 'Linear Support Vector Classifier':
            model = ExplainableLinearSVC()
        elif selected_model == 'Linear Stochastic Gradient Descent Classifier':
            model = ExplainableSGDClassifier()
        elif selected_model == 'Perceptron':
            model = ExplainablePerceptron()
        else:
            model = ExplainableLinearSVC() # default case, in case of some error

        X, Y, plotData, chartLayout = plotmaker.makeIris(obs) #plotmaker.make(uploaded_file_url, obs, int_idxs, str_idxs)

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

        return render(request, 'explainable/flip.html', {"module" : module, "stage" : 5, "uploaded_file_url" : uploaded_file_url, "selected_model" : selected_model, "int_idxs" : int_idxs, "str_idxs" : str_idxs, "chart" : myChart})
    else:
        return render(request, 'explainable/flip.html', {"module" : module, "stage" : -1})
