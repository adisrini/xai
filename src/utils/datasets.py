import csv

class Datasets:
    
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
    
    def load_iris(self):
        X = []
        y = []
        with open('../res/datasets/iris.data', 'rt') as f:
            reader = csv.reader(f, delimiter = ',', )
            for ln in reader:
                features = []
                for i in range(len(ln)):
                    if i in [1, 2, 3, 4]:
                        features.append(float(ln[i]))
                    else:
                        features.append(ln[i])
                X.append(features)
        return X, y
        