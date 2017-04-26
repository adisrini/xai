import numpy as np
import plotly.graph_objs as go
from ..utils.datasets import Datasets

def hyperplane(coefs, idxs, obs):
    unused_obs = [(i, x) for i, x in enumerate(obs) if i not in idxs]
    x_coef = coefs[0][idxs[0]]
    y_coef = coefs[0][idxs[1]]
    z_coef = coefs[0][idxs[2]]
    def z(x, y):
        return (-x*x_coef - y*y_coef)/z_coef

    data = []
    for y in range(0, 10):
        row = []
        for x in range(0, 10):
            row.append(z(x, y))
        data.append(row)

    return [go.Surface(z = data, type='surface', opacity = 0.7)]

def make(features, labels, obs, idxs):
    x_pos = [obs[idxs[0]] for idx, obs in enumerate(features) if labels[idx] == 1]
    y_pos = [obs[idxs[1]] for idx, obs in enumerate(features) if labels[idx] == 1]
    z_pos = [obs[idxs[2]] for idx, obs in enumerate(features) if labels[idx] == 1]

    x_neg = [obs[idxs[0]] for idx, obs in enumerate(features) if labels[idx] == -1]
    y_neg = [obs[idxs[1]] for idx, obs in enumerate(features) if labels[idx] == -1]
    z_neg = [obs[idxs[2]] for idx, obs in enumerate(features) if labels[idx] == -1]

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

    trace3 = go.Scatter3d(
        x=[obs[0][0]],
        y=[obs[0][1]],
        z=[obs[0][2]],
        mode='markers',
        marker=dict(
            size=6,
            line=dict(
                color='rgba(123, 210, 17, 0.14)',
                width=0.5
            ),
            opacity=0.8
        )
    )

    x_range = [min(min(x_pos), min(x_neg)), max(max(x_pos), max(x_neg))]
    y_range = [min(min(y_pos), min(y_neg)), max(max(y_pos), max(y_neg))]
    z_range = [min(min(z_pos), min(z_neg)), max(max(z_pos), max(z_neg))]

    layout = go.Layout(title="Explaining the Iris Dataset",
                       xaxis = dict(range=x_range),
                       yaxis = dict(range=y_range),
                       scene = dict(
                                    xaxis = dict(
                                        nticks=4, range = [4,7],),
                                    yaxis = dict(
                                        nticks=4, range = [2,5],),
                                    zaxis = dict(
                                        nticks=4, range = [0,5],),),
                      )

    return [trace1, trace2, trace3], layout


def makeIris(obs):
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

    trace3 = go.Scatter3d(
        x=[obs[0][0]],
        y=[obs[0][1]],
        z=[obs[0][2]],
        mode='markers',
        marker=dict(
            size=6,
            line=dict(
                color='rgba(123, 210, 17, 0.14)',
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

    return features, labels, [trace1, trace2, trace3], layout

def flip(explanation, obs):
    new_obs = []
    features = dict(explanation.features())
    for i in range(len(obs[0])):
        new_obs.append(obs[0][i] + features['feature ' + str(i)])
    print(new_obs)
    return [go.Scatter3d(x = [new_obs[0]],
                         y = [new_obs[1]],
                         z = [new_obs[2]],
                         mode='markers',
                         marker=dict(
                             size=6,
                             line=dict(
                                 color='rgba(200, 10, 21, 0.14)',
                                 width=0.5
                             ),
                             opacity=0.8
                         ))]
