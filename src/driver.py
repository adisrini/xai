import numpy as np
from scipy.optimize import linprog
from models.x_linearsgdc import ExplainableSGDClassifier #ExplainableSGDClassifier, ExplainableLinearSVC, ExplainablePerceptron, ExplainableSVC


if __name__ == '__main__':
    X = [['blue', ]]
    Y = [-1, -1, 1, 1]
    obs = [[4, 500]]
    model = ExplainableSGDClassifier()
    model.fit(X, Y)     
    print "predicted: ", model.predict(obs)[0]
    print "score:     ", model.score(X, Y)
    explanation = model.explain(obs)
    print explanation.top_k(5)
    print explanation.confidence()