from sklearn.linear_model import Perceptron
from explain import Explainer, ExplainableModel
from optimize import LPOptimizer

class ExplainablePerceptron(ExplainableModel):
    
    def __init__(self):
        self.reg = Perceptron()
        self.explainer = Explainer(LPOptimizer.optimize)
    
    def fit(self, X, y):
        """
        Trains the model with the provided training data.
        """
        self.reg.fit(X, y)
        self.data = X
    
    def predict(self, X):
        """
        Predicts the output given the trained model and an observation.
        """
        return self.reg.predict(X)
    
    def score(self, X, y):
        """
        Returns the coefficient of determination of the model.
        """
        return self.reg.score(X, y)
    
    def explain(self, X):
        """
        Returns an explanation given the trained model and an observation.
        """
        return self.explainer.explain(self.reg, self.data, X)