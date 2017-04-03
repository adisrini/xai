import unittest
from tests import encoding_test

def suite():
    suite = unittest.TestSuite()
    suite.addTest(encoding_test.suite())
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
    