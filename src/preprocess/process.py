from sklearn.preprocessing import LabelEncoder
import pandas as pd
from collections import defaultdict

class DataEncoder:
    
#     def fit(self, X):
#         self.n = len(X[0])
#         self.encoders = [LabelEncoder() for i in range(self.n)]
#         for i in range(self.n):
#             if type(X[0][i]) == str:
#                 self.encoders[i].fit([row[i] for row in X])
#     
#     def transform(self, X):
#         assert self.encoders is not None, "Encoders have not been initialized yet"
#         encX = [[] for i in range(len(X))]
#         for row in range(len(X)):
#             for i in range(self.n):
#                 item = X[row][i]
#                 if type(item) == str:
#                     encX[row].append(self.encoders[i].transform([item])[0])
#                 else:
#                     encX[row].append(item)
#         return encX
#         
#     def fit_transform(self, X):
#         self.fit(X)
#         return self.transform(X)
#     
#     def inverse_transform(self, encX):
#         X = [[] for i in range(len(encX))]
#         for row in range(len(encX)):
#             for i in range(self.n):
#                 item = encX[row][i]
#                 try:
#                     X[row].append(self.encoders[i].inverse_transform([item])[0])
#                 except:
#                     X[row].append(item)
#         return X
        
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
        
    def inverse_transform(self, encX):
        
        
    def from_dummies(data):
        '''
        The inverse transformation of ``pandas.get_dummies``.
    
        Parameters
        ----------
        data : DataFrame
        categories : Index or list of Indexes
        ordered : boolean or list of booleans
        prefixes : str or list of str
    
        Returns
        -------
        transformed : Series or DataFrame
    
        Notes
        -----
        To recover a Categorical, you must provide the categories and
        maybe whether it is ordered (default False). To invert a DataFrame that includes either
        multiple sets of dummy-encoded columns or a mixture of dummy-encoded
        columns and regular columns, you must specify ``prefixes``.
        '''
        return data