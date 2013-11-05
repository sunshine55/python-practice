import unittest
from booltrick import trickBooleans

class TestBoolTrick(unittest.TestCase):
    
    def setUp(self):
        self.ttt = (True, True, True)
        self.ttf = (True, True, False)
        self.tft = (True, False, True)
        self.tff = (True, False, False)
        self.ftt = (False, True, True)
        self.ftf = (False, True, False)
        self.fft = (False, False, True)
        self.fff = (False, False, False)

    def test_ttt(self):
        self.assertEqual(True, trickBooleans(*self.ttt))

    def test_ttf(self):
        self.assertEqual(True, trickBooleans(*self.ttf))

    def test_tft(self):
        self.assertEqual(True, trickBooleans(*self.tft))

    def test_tff(self):
        self.assertEqual(False, trickBooleans(*self.tff))

    def test_ftt(self):
        self.assertEqual(True, trickBooleans(*self.ftt))

    def test_ftf(self):
        self.assertEqual(False, trickBooleans(*self.ftf))

    def test_fft(self):
        self.assertEqual(False, trickBooleans(*self.fft))

    def test_fff(self):
        self.assertEqual(False, trickBooleans(*self.fff))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBoolTrick))    
    return suite


if __name__ == "__main__":
    # unittest.main()
    unittest.TextTestRunner(verbosity=2).run(suite())