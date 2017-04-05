from preprocess.string_binarizer import StringBinarizer
from sklearn.preprocessing import StandardScaler

class Preprocesser:
    
    def __init__(self):
        self.sb = StringBinarizer()
        self.ss = StandardScaler()
        
    def fit_transform(self, X):
        binarizedData = self.sb.fit_transform(X)
#         standardizedData = self.ss.fit_transform(X)
        return binarizedData
    
    def transform(self, obs):
        binarizedObservation = self.sb.transform(obs)
#         standardizedObservation = self.ss.transform(obs)
        return binarizedObservation
        
    def inverse_transform(self, encX):
        unbinarizedData = self.sb.inverse_transform(encX)
#         unstandardizedData = self.ss.inverse_transform(encX)
        return unbinarizedData