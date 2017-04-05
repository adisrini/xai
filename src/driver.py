import numpy as np
from scipy.optimize import linprog
from models.x_linearsgdc import ExplainableSGDClassifier
from models.x_linearsvc import ExplainableLinearSVC
from models.x_perceptron import ExplainablePerceptron

if __name__ == '__main__':
    X = [[0, 0], [1, 10], [2, 20], [3, 30], [4, 40]]
    Y = [-1, -1, -1, 1, 1]
    obs = [[100, 1000]]
    model = ExplainablePerceptron()
    model.fit(X, Y)     
    explanation = model.explain(obs)
    print explanation.features()
    print explanation.confidence()