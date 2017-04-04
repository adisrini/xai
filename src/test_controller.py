import unittest
from tests import binarizer_test

def suite():
    suite = unittest.TestSuite()
    suite.addTest(binarizer_test.suite())
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
    