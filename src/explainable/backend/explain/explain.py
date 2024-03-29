import operator

class Explanation:

    def __init__(self, observation, shifts, ranges):
        """
        Initializes an explanation with a dictionary from features to their shifts.
        """
        self.shifts = shifts
        self.ranges = ranges
        self.observation = observation
        self.EPSILON = 1e-5

    # TODO: sort by absolute value
    def top_k(self, k):
        """
        Returns the top k features ranked by amount shifted in descending order.
        """
        return sorted(self.shifts.items(), key = lambda v: abs(v[1]), reverse = True)[:k]

    def features(self):
        """
        Returns all features ranked by amount shifted in descending order.
        Equivalent to calling top_k(n) where n is the number of features
        """
        return sorted(self.shifts.items(), key = operator.itemgetter(1), reverse = True)[:]

    def confidence(self):
        """
        Returns a quantity representing the robustness of the model. A higher confidence value
        indicates a robust observation given the model. A lower confidence value indicates
        a volatile observation given the model.
        """
        total = 0
        count = 0
        n = len(self.observation[0])
        for i in range(n):
            if abs(self.shifts["feature " + str(i)]) > self.EPSILON:
                total = total + (abs(self.shifts["feature " + str(i)])/float(self.ranges[i]))
                count += 1
        return total/float(count)

class ExplainableModel(object):

    def fit(self, X, y):
        """
        Trains the model with the provided training data.
        """
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
