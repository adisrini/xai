import unittest
from preprocess.process import StringBinarizer

class BinarizerTest(unittest.TestCase):
    
    def setUp(self):
        print("Setting up...")
        self.pp = StringBinarizer()
        self.X = [['January', 40, 'Jake'], ['February', 80, 'Ferida'], ['March', 60, 'Mary'], ['March', 50, 'Michael']]
        self.encX = self.pp.fit_transform(self.X)
    
    def tearDown(self):
        print("Tearing down...")
        del self.X
     
    def testEncodeAndDecode(self):
        self.assertTrue(self.X == self.pp.inverse_transform(self.encX))
      
    def testTransform(self):
        encObs = self.pp.transform([['January', 40, 'Jake']])
        self.assertTrue(self.encX[0] == encObs[0])
         
    def testRounding(self):
        encObs = [[0.21, 0.69, 0, 40, 0, 0.88, 0.02, 0.1]]
        self.assertTrue(self.pp.inverse_transform(encObs) == [['January', 40, 'Jake']])
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BinarizerTest, 'test'))
    return suite