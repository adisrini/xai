import numpy as np
import datasets
from scipy.optimize import linprog
from x_linearsgdc import ExplainableSGDClassifier
from x_linearsvc import ExplainableLinearSVC
from x_perceptron import ExplainablePerceptron
from x_svc import ExplainableSVC

if __name__ == '__main__':
    X, Y = datasets.load_credit()
#     X = [[-2, -200], [0, 0], [1, 100], [2, 200]]
#     Y = [-1, -1, 1, 1]
    model = ExplainableSGDClassifier()
    model.fit(X, Y)
#     obs = [[-1000, -1000]]
    obs = [['b', 30.83, 0.0, 'u', 'g', 'w', 'v', 1.25, 't', 't', 1.0, 'f', 'g', 202.0, '0']]
#     
    explanation = model.explain(obs)
#      
#     print model.predict(obs)
#     print explanation.top_k(2)
#     print explanation.confidence()

#     X = [["January", 40.0], ["February", 50.0], ["August", 70.0]]
#     Y = [1, 1, -1]
#     model = ExplainableSGDClassifier()
#     model.fit(X, Y)