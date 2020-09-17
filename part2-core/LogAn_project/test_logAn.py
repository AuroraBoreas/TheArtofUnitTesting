from logAn import LogAnalyzer
import unittest
from unittest import mock

class TestLogAn(unittest.TestCase):
    def test_isValid_log_filename_1(self):
        la = LogAnalyzer('hello.SLF')
        self.assertFalse(la.isValid_log_filename())

    def test_isValid_log_filename_2(self):
        la = LogAnalyzer('hello.sth')
        self.assertTrue(la.isValid_log_filename())
        
    def test_isValid_log_filename_3(self):
        la = LogAnalyzer('hello_world')
        self.assertTrue(la.isValid_log_filename())
        self.assertTrue(la.wasLastFileNameValid)

    def test_isValid_log_filename_4(self):
        la = LogAnalyzer('whatever')
        self.assertTrue(la.isValid_log_filename())
        
    def test_isValid_log_filename_5(self):
        la = LogAnalyzer('')
        self.assertRaises(ValueError, la.isValid_log_filename)


if __name__ == "__main__":
    unittest.main()