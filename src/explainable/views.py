from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
import random
import plotly
import plotly.graph_objs as go
from .models import Module, Dataset, OverwriteStorage, ExplainableModel
from .backend.models.x_linearsvc import ExplainableLinearSVC
from .backend.utils.datasets import Datasets

def index(request):
    explainable_modules = Module.objects.all()
    context = {
        'modules' : explainable_modules
    }
    return render(request, 'explainable/index.html', context)

def example(request):
    X, Y = Datasets.load_iris()
    Xp, Yp = Datasets.binarize(X, Y, 'Iris-setosa', 'Iris-versicolor')
    obs = [[random.uniform(4, 7),
            random.uniform(2, 4),
            random.uniform(3, 5.5),
            random.uniform(0, 2)]]
    model = ExplainableLinearSVC()
    model.fit(Xp, Yp)
    explanation = model.explain(obs)
    myChart = plotly.offline.plot({
        "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
        "layout": go.Layout(title="hello world", autosize=True)
        },output_type="div", show_link="False",include_plotlyjs="Flase",link_text="")
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
