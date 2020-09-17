from simple_parser import SimpleParser
import unittest
# from unittest import mock

class TestSimpleParser(unittest.TestCase):
    # def setUp(self):
    #     print('set up')
    # def tearDown(self):
    #     print('tear down')

    def test_parser_and_sum_empty_string(self):
        sp = SimpleParser('')
        self.assertEqual(0, sp.parse_and_sum())
    def test_parser_and_sum_no_comma(self):
        sp = SimpleParser('1')
        self.assertEqual(1, sp.parse_and_sum())
    def test_parser_and_sum_minus(self):
        sp = SimpleParser('-1')
        self.assertEqual(-1, sp.parse_and_sum())
    def test_parser_and_sum_with_comma(self):
        sp = SimpleParser('1, 2')
        self.assertRaises(ValueError, sp.parse_and_sum)

if __name__ == "__main__":
    unittest.main()

