def ranges(data, X):
        featureRanges = []
        for i in range(len(X[0])):
            lst = [f[i] for f in data]
            featureRanges.append(max(max(lst), X[0][i]) - min(min(lst), X[0][i]))
        return featureRanges