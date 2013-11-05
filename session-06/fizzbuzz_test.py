import unittest
from fizzbuzz import outputFizzBuzz

class TestFizzBuzz(unittest.TestCase):
    
    def setUp(self):
        self.numbers = range(1, 16)
    
    def test_output(self):
        correct = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        self.assertEqual(correct, outputFizzBuzz(self.numbers))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFizzBuzz))    
    return suite


if __name__ == "__main__":
    # unittest.main()
    unittest.TextTestRunner(verbosity=2).run(suite())