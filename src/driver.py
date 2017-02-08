import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from x_sgdc import ExplainableSGDClassifier

EPSILON = 0.001

if __name__ == '__main__':
    X = np.array([[-1, -1], [0, 0], [1, 1], [2, 2]])
    Y = np.array([-1, -1, 1, 1])
    model = ExplainableSGDClassifier()
    model.fit(X, Y)
    coefs = model.reg.coef_[0]
    b1 = coefs[0]
    b2 = coefs[1]
    b0 = model.reg.intercept_[0]
    n = X[0].size
    
    print b0
    print b1
    print b2
    
    observation = [[0, 0]]
    
    label = model.predict(observation)[0]
    
    c = [0 for _ in range(n)] + [1 for _ in range(n)]
        
    A_ineq = []
    for i in range(n):
        row1 = [0 for _ in range(2*n)]; row1[i] = -1; row1[n + i] = -1
        row2 = [0 for _ in range(2*n)]; row2[i] = 1; row2[n + i] = -1
        A_ineq.append(row1)
        A_ineq.append(row2)
    
    A_ineq.append([label*coefs[i] for i in range(n)] + [0 for i in range(n)])
    
    b_ineq = [f(x) for x in observation[0] for f in (lambda x: -x, lambda x: x)] + [label * -model.reg.intercept_[0] + label * EPSILON]
    
    bnds = ()
    for i in range(2*n):
        bnds = ((None, None),) + bnds
    
    res = linprog(c, A_ub = A_ineq, b_ub = b_ineq, bounds = bnds, options={"disp": True})
    print res
    
    print model.predict(observation)
    print model.predict([[res.x[0], res.x[1]]])