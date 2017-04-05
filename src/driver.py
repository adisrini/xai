import numpy as np
from scipy.optimize import linprog
from models.x_linearsgdc import ExplainableSGDClassifier
from models.x_linearsvc import ExplainableLinearSVC
from models.x_perceptron import ExplainablePerceptron

if __name__ == '__main__':
    X = [[1, 10], [2, 20], [3, 30], [4, 40]]
    Y = [-1, -1, 1, 1]
    obs = [[20, 200]]
    model = ExplainableLinearSVC()
    model.fit(X, Y)     
    print "predicted: ", model.predict(obs)
#     print "score:     ", model.score(X, Y)
    explanation = model.explain(obs)
    print explanation.top_k(5)
    print explanation.confidence()