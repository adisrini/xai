from .string_binarizer import StringBinarizer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer
import numpy as np

class Preprocesser:

    def __init__(self):
        self.sb = StringBinarizer()
        self.ss = StandardScaler()
        self.lb = LabelBinarizer(neg_label = -1, pos_label = 1)

    def fit_transform(self, X):
        binarizedData = self.sb.fit_transform(X)
#         standardizedData = self.ss.fit_transform(X)
        return binarizedData

    def label_fit_transform(self, Y):
        binarizedLabels = list(np.array(self.lb.fit_transform(Y)).transpose()[0])
        return binarizedLabels

    def transform(self, obs):
        binarizedObservation = self.sb.transform(obs)
#         standardizedObservation = self.ss.transform(obs)
        return binarizedObservation

    def label_transform(self, Y):
        binarizedLabel = self.lb.transform(Y)
        return binarizedLabel

    def inverse_transform(self, encX):
        unbinarizedData = self.sb.inverse_transform(encX)
#         unstandardizedData = self.ss.inverse_transform(encX)
        return unbinarizedData

    def label_inverse_transform(self, encY):
        unbinarizedLabel = self.lb.inverse_transform(encY)
        return unbinarizedLabel
