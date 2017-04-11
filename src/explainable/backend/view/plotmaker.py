import numpy as np
import plotly.graph_objs as go
from ..utils.datasets import Datasets

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

    layout = go.Layout(title="Explaining the Iris Dataset", autosize=True)

    return features, labels, [trace1, trace2], layout
