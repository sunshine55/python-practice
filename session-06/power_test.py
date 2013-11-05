import unittest
from power import isPowerOfTwo
from ddt import ddt, data

@ddt
class TestPower(unittest.TestCase):
    
    @data(0, 1, 2, 64)
    def testIsPowerOfTwo(self, value):
        self.assertTrue(isPowerOfTwo(value))
    
    @data(6, 63, '2', 2.64)
    def testIsNotPowerOfTwo(self, value):
        self.assertFalse(isPowerOfTwo(value))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()