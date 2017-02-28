import operator

class Explanation:
    
    def __init__(self, observation, shifts, ranges):
        """
        Initializes an explanation with a dictionary from features to their shifts.
        """
        self.shifts = shifts
        self.ranges = ranges
        self.observation = observation
        
    def top_k(self, k):
        """
        Returns the top k features ranked by amount shifted.
        """
        return sorted(self.shifts.items(), key = operator.itemgetter(1), reverse = True)[:k]
    
    def confidence(self):
        """
        Returns a quantity representing the robustness of the model. A higher confidence value
        indicates a robust observation given the model. A lower confidence value indicates
        a volatile observation given the model.
        """
        total = 0
        n = len(self.observation[0])
        for i in range(n):
            total = total + (self.shifts["feature " + str(i)])/float(self.ranges[i])
        return total/float(n)

class ExplainableModel(object):
    
    def fit(self, X, y):
        """
        Trains the model with the provided training data.
        """
        # preprocess
        pass
        
    def predict(self, X):
        """
        Predicts the output given the trained model and an observation.
        """
        pass
    
    def score(self, X, y):
        """
        Returns the coefficient of determination of the model.
        """
        pass
        
    def explain(self, X):
        """
        Returns an explanation given the trained model and an observation.
        """
        pass
    
class Explainer:
    
    def __init__(self, optimizer):
        self.optimizer = optimizer
    
    def explain(self, model, data, X):
        """
        Returns an Explanation given a model and an observation
        """
        shifts, ranges = self.optimizer.optimize(model, data, X)
        return Explanation(X, shifts, ranges)
    