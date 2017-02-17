import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from x_linearsgdc import ExplainableSGDClassifier
from x_linearsvc import ExplainableSVC

if __name__ == '__main__':
    X = np.array([[-2, -200], [0, 0], [1, 100], [2, 200]])
    Y = np.array([-1, -1, 1, 1])
    model = ExplainableSVC()
    model.fit(X, Y)
    obs = [[-1000, -1000]]
    explanation = model.explain(obs)
    print explanation.top_k(2)
    print explanation.confidence()