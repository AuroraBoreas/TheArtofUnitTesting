from logan1 import LogAnalyzer
import unittest

class TestLogAnalyzer(unittest.TestCase):
    def test_isValid_log_filename_1(self):
        la = LogAnalyzer()
        self.assertTrue(la.isValid_log_filename('readme.md'))
    def test_isValid_log_filename_2(self):
        la = LogAnalyzer()
        self.assertFalse(la.isValid_log_filename('hello?'))

if __name__ == "__main__":
    unittest.main()