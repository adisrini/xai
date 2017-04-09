import csv

class Datasets:
    
    @staticmethod
    def load_credit(self):
        X = []
        y = []
        with open('../res/datasets/crx.data', 'rt') as f:
            reader = csv.reader(f, delimiter = ',', )
            for ln in reader:
                features = []
                for i in range(len(ln)):
                    if i in [1, 2, 7, 10, 13, 14]:
                        features.append(float(ln[i]))
                    elif i in [15]:
                        y.append(1 if ln[i] == '+' else -1)
                    else:
                        features.append(ln[i])
                X.append(features)
        return X, y
    
    @staticmethod
    def load_iris():
        X = []
        y = []
        with open('../res/datasets/iris.data', 'rt') as f:
            reader = csv.reader(f, delimiter = ',', )
            for ln in reader:
                features = []
                for i in range(len(ln)):
                    if i in [0, 1, 2, 3]:
                        features.append(float(ln[i]))
                    else:
                        y.append(ln[i])
                X.append(features)
        return X, y
    
    @staticmethod
    def binarize(X, y, label1, label2):
        Xp = []
        yp = []
        assert len(X) == len(y)
        for i in range(len(X)):
            if(y[i] == label1 or y[i] == label2):
                Xp.append(X[i])
                yp.append(1 if y[i] == label1 else -1)
        return Xp, yp
        