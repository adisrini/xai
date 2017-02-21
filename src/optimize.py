from scipy.optimize import linprog

class Optimizer:
    def optimize(self, model, data, X):
        pass
    
class PatternSearchOptimizer:
    
    def __init__(self):
        self.EPSILON = 0.001
        
    def optimize(self, model, data, X):
        assert len(X) == 1
        assert len(model.coef_) == 1
    
class LPOptimizer:
    
    def __init__(self):
        self.EPSILON = 0.001
    
    def ranges(self, data, X):
        featureRanges = []
        for i in range(len(X[0])):
            lst = [f[i] for f in data]
            featureRanges.append(max(max(lst), X[0][i]) - min(min(lst), X[0][i]))
        return featureRanges
    
    def shifts(self, X, result):
        shifts = {}
        for i in range(len(X[0])):
            shifts["feature " + str(i)] = abs(X[0][i] - result.x[i])
        return shifts
    
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
        
        b_ineq = [f(X[0][i]/float(ranges[i])) for i in range(n) for f in (lambda x: -x, lambda x: x)] + [label * -intercept + label * self.EPSILON]
        
        bnds = ()
        for i in range(2*n):
            bnds = ((None, None),) + bnds
        
        return linprog(c, A_ub = A_ineq, b_ub = b_ineq, bounds = bnds, options={"disp": True})
    
    def optimize(self, model, data, X):
        assert len(X) == 1
        assert len(model.coef_) == 1
        
        featureRanges = self.ranges(data, X)
        result = self.linprog(model, X, featureRanges)
        print result
        
        shifts = self.shifts(X, result)
        return (shifts, featureRanges)
        
    