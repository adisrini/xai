import operator
from scipy.optimize import linprog

EPSILON = 0.001

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

class ExplainableModel:
    
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
    
    def ranges(self, data, X):
        featureRanges = []
        for i in range(len(X[0])):
            lst = [f[i] for f in data]
            featureRanges.append(max(max(lst), X[0][i]) - min(min(lst), X[0][i]))
        return featureRanges
    
    def linprog(self, model, X, ranges):
        n = len(X[0])
        coefs = model.coef_[0]
        assert len(coefs) == n
        intercept = model.intercept_[0]
        label = model.predict(X)[0]
        c = [0 for _ in range(n)] + [1 for i in range(n)]
            
        A_ineq = []
        for i in range(n):
            row1 = [0 for _ in range(2*n)]; row1[i] = -1/float(ranges[i]); row1[n + i] = -1
            row2 = [0 for _ in range(2*n)]; row2[i] = 1/float(ranges[i]); row2[n + i] = -1
            A_ineq.append(row1)
            A_ineq.append(row2)
        
        A_ineq.append([label*coefs[i] for i in range(n)] + [0 for i in range(n)])
        
        b_ineq = [f(X[0][i]/float(ranges[i])) for i in range(n) for f in (lambda x: -x, lambda x: x)] + [label * -intercept + label * EPSILON]
        
        bnds = ()
        for i in range(2*n):
            bnds = ((None, None),) + bnds
        
        return linprog(c, A_ub = A_ineq, b_ub = b_ineq, bounds = bnds, options={"disp": True})
    
    def shifts(self, X, result):
        shifts = {}
        for i in range(len(X[0])):
            shifts["feature " + str(i)] = abs(X[0][i] - result.x[i])
        return shifts
    
    def explain(self, model, data, X):
        """
        Returns an Explanation given a model and an observation
        """
        assert len(X) == 1
        assert len(model.coef_) == 1
        
        featureRanges = self.ranges(data, X)
        result = self.linprog(model, X, featureRanges)
        print result
        
        shifts = self.shifts(X, result)
        return Explanation(X, shifts, featureRanges)