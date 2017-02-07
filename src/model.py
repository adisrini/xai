import operator

class Explanation:
    
    def __init__(self, shifts):
        """
        Initializes an explanation with a dictionary from features to their shifts.
        """
        self.shifts = shifts
        
    def top_k(self, k):
        """
        Returns the top k features ranked by amount shifted.
        """
        return sorted(self.shifts.items(), key = operator.itemgetter(1), reverse = True)[:k]

class ExplainableModel:
    
    def fit(self, X, y):
        """
        Trains the model with the provided training data.
        """
        raise NotImplementedError()
    
    def predict(self, X):
        """
        Predicts the output given the trained model and an observation.
        """
        raise NotImplementedError()
    
    def score(self, X, y):
        """
        Returns the coefficient of determination of the model.
        """
        raise NotImplementedError()
    
    def explain(self, X):
        """
        Returns an explanation given the trained model and an observation.
        """
        raise NotImplementedError()
    
class Explainer:
    
    def explain(self, model, X):
        """
        Returns an Explanation given a model and an observation
        """