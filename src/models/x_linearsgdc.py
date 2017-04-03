from sklearn.linear_model import SGDClassifier
from explain.explain import Explainer, ExplainableModel
from optimize.optimize import LPOptimizer
from preprocess.process import DataEncoder

class ExplainableSGDClassifier(ExplainableModel):
    
    def __init__(self):
        self.reg = SGDClassifier()
        self.explainer = Explainer(LPOptimizer())
        self.de = DataEncoder()
    
    def fit(self, X, y):
        """
        Trains the model with the provided training data.
        """
        encX = self.de.fit_transform(X)
        self.reg.fit(encX, y)
        self.data = encX
    
    def predict(self, X):
        """
        Predicts the output given the trained model and an observation.
        """
        encX = self.de.transform(X)
        return self.reg.predict(encX)
    
    def score(self, X, y):
        """
        Returns the coefficient of determination of the model.
        """
        return self.reg.score(self.de.transform(X), y)
    
    def explain(self, X):
        """
        Returns an explanation given the trained model and an observation.
        """
        return self.explainer.explain(self.reg, self.data, self.de.transform(X))