from sklearn.svm import LinearSVC
import numpy as np
from ..explain.explain import Explainer, ExplainableModel
from ..optimize.optimize import LPOptimizer
from ..preprocess.process import Preprocesser

class ExplainableLinearSVC(ExplainableModel):

    def __init__(self):
        self.reg = LinearSVC()
        self.explainer = Explainer(LPOptimizer())
        self.pp = Preprocesser()

    def fit(self, X, y):
        """
        Trains the model with the provided training data.
        """
        encX = self.pp.fit_transform(X)
        self.reg.fit(encX, y)
        self.data = encX

    def predict(self, X):
        """
        Predicts the output given the trained model and an observation.
        """
        encX = self.pp.transform(X)
        return self.reg.predict(encX)

    def score(self, X, y):
        """
        Returns the coefficient of determination of the model.
        """
        return self.reg.score(self.pp.transform(X), y)

    def coefs(self):
        return np.concatenate((self.reg.intercept_, self.reg.coef_[0]), axis = 0)

    def explain(self, X):
        """
        Returns an explanation given the trained model and an observation.
        """
        return self.explainer.explain(self.reg, self.data, self.pp.transform(X))
