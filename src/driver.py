import numpy as np
from scipy.optimize import linprog
from models import ExplainableSGDClassifier, ExplainableLinearSVC, ExplainablePerceptron, ExplainableSVC

if __name__ == '__main__':
    X = [[-2, -200], [0, 0], [1, 100], [2, 200]]
    Y = [-1, -1, 1, 1]
    model = ExplainableLinearSVC()
    model.fit(X, Y)     
    print model.predict(obs)
    print model.score(X, Y)
    explanation = model.explain(obs)
    print explanation.top_k(5)
    print explanation.confidence()
#      
#     print model.predict(obs)
#     print explanation.top_k(2)
#     print explanation.confidence()