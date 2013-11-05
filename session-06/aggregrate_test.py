import unittest, booltrick_test, fizzbuzz_test, power_test

suite1 = booltrick_test.suite()
suite2 = fizzbuzz_test.suite()
suite3 = power_test.suite()

suite = unittest.TestSuite()
suite.addTests([suite1, suite2, suite3])

unittest.TextTestRunner(verbosity=2).run(suite)