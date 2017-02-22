from scipy.optimize import linprog
from copy import deepcopy
import random
import util
import numpy as np

class Optimizer:
    def optimize(self, model, data, X):
        pass
    
class PatternSearchOptimizer:
    
    class SearchNode:
        def __init__(self, state):
            self.state = state
            
        def successors(self, explore_idxs, deltas):
            succs = []
            for i in explore_idxs:
                pos_delta_assignments = deepcopy(self.state)
                pos_delta_assignments[0][i] += deltas[i]
                succs.append(pos_delta_assignments)
                neg_delta_assignments = deepcopy(self.state)
                neg_delta_assignments[0][i] -= deltas[i]
                succs.append(neg_delta_assignments)
            return succs
        
        def __repr__(self):
            return "{" + str(self.state) + "}"
        
        def __hash__(self):
            return hash(str(self.state))
    
        def __eq__(self, other):
            if isinstance(other, type(self)):
                return self.state == other.state
            else:
                return False
    
    def __init__(self):
        self.EPSILON = 0.001
        self.FACTOR = float(50)
        
    def optimize(self, model, data, X):
        assert len(X) == 1
        deltas = [range/self.FACTOR for range in util.ranges(data, X)]
        label = model.predict(X)[0]
                        
        visited = set()
        root = self.SearchNode(X)
        visited.add(root)
        q = [root]
        while len(q) > 0:
            n = q.pop(0)
            succs = n.successors([0, 1], deltas)
            for succ in succs:
                c = self.SearchNode(succ)
                if not(model.predict(c.state)[0] == label):
                    print "Path found!"
                    print c.state
                    print model.predict(c.state)[0]
                    print label
                    return {}, []
                if c not in visited:
                    q.append(c)
                    visited.add(c)
        print "No path found!"
        
        return {}, []
    
class LPOptimizer:
        
    def __init__(self):
        self.EPSILON = 0.001
    
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
        
        featureRanges = util.ranges(data, X)
        result = self.linprog(model, X, featureRanges)
        print result
        
        shifts = self.shifts(X, result)
        return (shifts, featureRanges)
        
    