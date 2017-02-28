from sklearn.preprocessing import LabelEncoder

class DataEncoder:
    
    def encode(self, X):
        self.n = len(X[0])
        self.encoders = [LabelEncoder() for i in range(self.n)]
        for i in range(self.n):
            if type(X[0][i]) == str:
                self.encoders[i].fit([row[i] for row in X])
    
    def transform(self, X):
        assert self.encoders is not None, "Encoders have not been initialized yet"
        encX = [[] for i in range(len(X))]
        for row in range(len(X)):
            for i in range(self.n):
                item = X[row][i]
                if type(item) == str:
                    encX[row].append(self.encoders[i].transform([item])[0])
                else:
                    encX[row].append(item)
        return encX
        
    def encode_transform(self, X):
        self.encode(X)
        return self.transform(X)
        
    
if __name__ == '__main__':
    X = [['January', 40], ['February', 80], ['March', 60], ['March', 50]]
    Y = [1, -1, -1, 1]
    de = DataEncoder()
    encX = de.encode_transform(X)