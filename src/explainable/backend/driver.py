import numpy as np
import random
from scipy.optimize import linprog
from .utils.datasets import Datasets
from .models.x_linearsgdc import ExplainableSGDClassifier
from .models.x_linearsvc import ExplainableLinearSVC
from .models.x_perceptron import ExplainablePerceptron

if __name__ == '__main__':
    X, Y = Datasets.load_iris()
    Xp, Yp = Datasets.binarize(X, Y, 'Iris-setosa', 'Iris-versicolor')
    obs = [[random.uniform(4, 7),
            random.uniform(2, 4),
            random.uniform(3, 5.5),
            random.uniform(0, 2)]]
    model = ExplainableLinearSVC()
    model.fit(Xp, Yp)
    explanation = model.explain(obs)
    print explanation.features()
    print explanation.confidence()
