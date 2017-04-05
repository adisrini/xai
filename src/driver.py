import numpy as np
from scipy.optimize import linprog
from utils.datasets import Datasets
from models.x_linearsgdc import ExplainableSGDClassifier
from models.x_linearsvc import ExplainableLinearSVC
from models.x_perceptron import ExplainablePerceptron

if __name__ == '__main__':
    X, Y = Datasets.load_iris()
    Xp, Yp = Datasets.binarize(X, Y, 'Iris-setosa', 'Iris-versicolor')
    print Xp
    print Yp
#     X = [[0, 0], [1, 10], [2, 20], [3, 30], [4, 40]]
#     Y = [-1, -1, -1, 1, 1]
#     obs = [[100, 1000]]
#     model = ExplainablePerceptron()
#     model.fit(X, Y)     
#     explanation = model.explain(obs)
#     print explanation.features()
#     print explanation.confidence()