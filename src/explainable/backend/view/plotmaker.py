import numpy as np
import plotly.graph_objs as go
from ..utils.datasets import Datasets

def hyperplane(coefs):
    x_coef = coefs[0][0]
    y_coef = coefs[0][1]
    z_coef = coefs[0][2]
    def z(x, y):
        return (-x*x_coef - y*y_coef)/z_coef

    data = []
    for y in range(0, 10):
        row = []
        for x in range(0, 10):
            row.append(z(x, y))
        data.append(row)

    return [go.Surface(z = data, type='surface', opacity = 0.7)]

def makeIris():
    f, l = Datasets.load_iris()
    features, labels = Datasets.binarize(f, l, 'Iris-setosa', 'Iris-versicolor')

    x_pos = [obs[0] for idx, obs in enumerate(features) if labels[idx] == 1]
    y_pos = [obs[1] for idx, obs in enumerate(features) if labels[idx] == 1]
    z_pos = [obs[2] for idx, obs in enumerate(features) if labels[idx] == 1]

    x_neg = [obs[0] for idx, obs in enumerate(features) if labels[idx] == -1]
    y_neg = [obs[1] for idx, obs in enumerate(features) if labels[idx] == -1]
    z_neg = [obs[2] for idx, obs in enumerate(features) if labels[idx] == -1]

    trace1 = go.Scatter3d(
        x=x_pos,
        y=y_pos,
        z=z_pos,
        mode='markers',
        marker=dict(
            size=6,
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=0.8
        )
    )

    trace2 = go.Scatter3d(
        x=x_neg,
        y=y_neg,
        z=z_neg,
        mode='markers',
        marker=dict(
            size=6,
            line=dict(
                color='rgba(123, 19, 210, 0.14)',
                width=0.5
            ),
            opacity=0.8
        )
    )

    layout = go.Layout(title="Explaining the Iris Dataset",
                       xaxis = dict(range=[min(min(x_pos), min(x_neg)), max(max(x_pos), max(x_neg))]),
                       yaxis = dict(range=[min(min(y_pos), min(y_neg)), max(max(y_pos), max(y_neg))]),
                       scene = dict(
                                    xaxis = dict(
                                        nticks=4, range = [4,7],),
                                    yaxis = dict(
                                        nticks=4, range = [2,5],),
                                    zaxis = dict(
                                        nticks=4, range = [0,5],),),
                      )

    return features, labels, [trace1, trace2], layout
