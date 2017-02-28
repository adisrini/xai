import csv

def load_credit():
    X = []
    y = []
    with open('../res/datasets/crx.data', 'rt') as f:
        reader = csv.reader(f, delimiter = ',', )
        for ln in reader:
            features = []
            for i in range(len(ln)):
                if ln[i] == '?':
                    features.append(None)
                    continue
                if i in [1, 2, 7, 10, 13]:
                    features.append(float(ln[i]))
                elif i in [15]:
                    y.append(1 if ln[i] == '+' else -1)
                else:
                    features.append(ln[i])
            X.append(features)
    return X, y