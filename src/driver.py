import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from x_sgdc import ExplainableSGDClassifier

if __name__ == '__main__':
    X = np.array([[-2, -1], [0, 0], [1, 1], [2, 2]])
    Y = np.array([-1, -1, 1, 1])
    model = ExplainableSGDClassifier()
    model.fit(X, Y)
    obs = [[0.5, 0.5]]
    explanation = model.explain(obs)
    print explanation.top_k(2)
    print explanation.confidence()