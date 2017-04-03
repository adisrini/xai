import pandas as pd

class DataEncoder:
        
    def fit_transform(self, X):
        self.num_features = len(X[0])
        encX = []
        self.dummies = dict()
        for i in range(self.num_features):
            if type(X[0][i]) == str:
                self.dummies[i] = pd.get_dummies([row[i] for row in X])     # add dummies dataframe to dictionary with feature # as key
        self.n = len(X)
        for i in range(self.n):
            obs = []
            for v in range(self.num_features):
                if type(X[i][v]) == str:
                    for cname in self.dummies[v].columns:
                        obs.append(self.dummies[v].iloc[i][cname])
                else:
                    obs.append(X[i][v])                
            encX.append(obs)
        return encX
    
    def transform(self, X):
        encX = []
        for i in range(len(X)):
            encObs = []
            for v in range(self.num_features):
                if type(X[i][v]) == str:
                    for cname in self.dummies[v].columns:
                        if(X[i][v] == cname):
                            encObs.append(1)
                        else:
                            encObs.append(0)
                else:
                    encObs.append(X[i][v])     
            encX.append(encObs)           
        return encX
        
    def inverse_transform(self, encX):
        X = []
        for i in range(self.n):
            obs = []
            actual_index = 0
            for j in range(self.num_features):
                if j in self.dummies:
                    dummy_matrix = self.dummies[j]
                    obs.append(dummy_matrix.columns[(i for i,v in enumerate([x for x in dummy_matrix.iloc[i]]) if v == 1).next()])
                    actual_index += len(dummy_matrix.columns)
                else:
                    obs.append(encX[i][actual_index])
                    actual_index += 1
            X.append(obs)
        return X