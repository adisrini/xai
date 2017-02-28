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
    obs = [['b', 20.67, 5.29,'u','g','q','v', 0.375, 't', 't', 01,'f', 'g', 00160, 0]]
#     
    print model.predict(obs)
    print model.score(X, Y)
#     explanation = model.explain(obs)
#      
#     print model.predict(obs)
#     print explanation.top_k(2)
#     print explanation.confidence()

#     X = [["January", 40.0], ["February", 50.0], ["August", 70.0]]
#     Y = [1, 1, -1]
#     model = ExplainableSGDClassifier()
#     model.fit(X, Y)