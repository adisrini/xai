from scipy.optimize import linprog
from copy import deepcopy
from queue import PriorityQueue
import random
from ..utils.functions import Functions
import numpy as np

class Optimizer:
    def optimize(self, model, data, X):
        pass

class PatternSearchOptimizer:

    class SearchNode:
        def __init__(self, state, cost):
            self.state = state
            self.cost = cost

        def successors(self, explore_idxs, deltas):
            succs = []
            for i in explore_idxs:
                pos_delta_assignments = deepcopy(self.state)
                pos_delta_assignments[0][i] += deltas[i]
                succs.append(self.__class__(pos_delta_assignments, deltas[i]))
                neg_delta_assignments = deepcopy(self.state)
                neg_delta_assignments[0][i] -= deltas[i]
                succs.append(self.__class__(neg_delta_assignments, deltas[i]))
            return succs

        def __repr__(self):
            return str(self.state)

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
        self.MAX_ITER = 10

    def optimize(self, model, data, X):
        assert len(X) == 1
        deltas = [range/self.FACTOR for range in Functions.ranges(data, X)]
        label = model.predict(X)[0]

        should_be_different = True
        iter = 0

        visited = set()
        root = self.SearchNode(X, 0)
        visited.add(root)
        q = [root]
        while len(q) > 0:
            n = q.pop(0)
            succs = n.successors([0, 1], deltas)
            for succ in succs:
                if not((model.predict(succ.state)[0] == label) == should_be_different):
                    print("Flip")
                    deltas = [d/float(2) for d in deltas]
                    should_be_different = not should_be_different
                    iter += 1
                    if iter > self.MAX_ITER:
                        print("Path found!")
                        print(succ.state)
                        print(model.predict(succ.state)[0])
                        print(label)
                        return {}, []
                if succ not in visited:
                    q.append(succ)
                    visited.add(succ)
        print("No path found!")

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
            row1 = [0 for _ in range(2*n)]; row1[i] = -1; row1[n + i] = -1
            row2 = [0 for _ in range(2*n)]; row2[i] = 1; row2[n + i] = -1
            A_ineq.append(row1)
            A_ineq.append(row2)

        A_ineq.append([label*coefs[i] for i in range(n)] + [0 for i in range(n)])

        b_ineq = [f(X[0][i]) + self.EPSILON for i in range(n) for f in (lambda x: -x, lambda x: x)] + [label * (-intercept) - self.EPSILON]

        bnds = ()
        for i in range(n):
            bnds = bnds + ((None, ranges[i]),)
        for i in range(n):
            bnds = ((None, None), ) + bnds

        return linprog(c, A_ub = A_ineq, b_ub = b_ineq, bounds = bnds, options={"disp": True, "bland": True, "tol": 1e-8})

    def optimize(self, model, data, X):
        assert len(X) == 1
        assert len(model.coef_) == 1

        featureRanges = Functions.ranges(data, X)
        result = self.linprog(model, X, featureRanges)
        print(result)

        print("original prediction: ", model.predict(X))
        print("flipped prediction:  ", model.predict([result.x[0:len(X[0])]]))

        shifts = self.shifts(X, result)
        return (shifts, featureRanges)
