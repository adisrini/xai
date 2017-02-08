from scipy.optimize import linprog

if __name__ == '__main__':
    b0 = -9.94047660383
    b1 = 19.6270853778
    b2 = 19.6270853778
    obs = [[1000, 1000]]
    x1 = obs[0][0]
    x2 = obs[0][1]
    y = 1
    
    # x1', x2', t1, t2
    
    c = [0, 0, 1, 1]
    A_i = [[-1, 0, -1, 0],
           [1, 0, -1, 0],
           [0, -1, 0, -1],
           [0, 1, 0, -1],
           [b1, b2, 0, 0]]
    b_i = [-x1, x1, -x2, x2, -b0]
    res = linprog(c, A_i, b_i, bounds = ((None, None), (None, None), (None, None), (None, None)), options={"disp": True})
    print res