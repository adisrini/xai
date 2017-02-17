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
    
    def explain(self, model, data, X):
        """
        Returns an Explanation given a model and an observation
        """
        assert len(X) == 1
        assert len(model.coef_) == 1
        
        n = len(X[0])
        coefs = model.coef_[0]
        intercept = model.intercept_[0]
        assert len(coefs) == n
        label = model.predict(X)[0]
        
        ranges = []
        for i in range(n):
            lst = [f[i] for f in data]
            ranges.append(max(max(lst), X[0][i]) - min(min(lst), X[0][i]))
                    
        c = [0 for _ in range(n)] + [1 for _ in range(n)]
            
        A_ineq = []
        for i in range(n):
            row1 = [0 for _ in range(2*n)]; row1[i] = -1; row1[n + i] = -1
            row2 = [0 for _ in range(2*n)]; row2[i] = 1; row2[n + i] = -1
            A_ineq.append(row1)
            A_ineq.append(row2)
        
        A_ineq.append([label*coefs[i] for i in range(n)] + [0 for i in range(n)])
        
        b_ineq = [f(x) for x in X[0] for f in (lambda x: -x, lambda x: x)] + [label * -intercept + label * EPSILON]
        
        bnds = ()
        for i in range(2*n):
            bnds = ((None, None),) + bnds
        
        res = linprog(c, A_ub = A_ineq, b_ub = b_ineq, bounds = bnds, options={"disp": True})
        print res
        
        print model.predict(X)
        print model.predict([[res.x[0], res.x[1]]])
        
        shifts = {}
        for i in range(n):
            shifts["feature " + str(i)] = abs(X[0][i] - res.x[i])
            
        return Explanation(X, shifts, ranges)