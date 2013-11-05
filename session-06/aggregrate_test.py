import unittest, booltrick_test, fizzbuzz_test

suite1 = booltrick_test.suite()
suite2 = fizzbuzz_test.suite()

suite = unittest.TestSuite()
suite.addTests([suite1, suite2])

unittest.TextTestRunner(verbosity=2).run(suite)