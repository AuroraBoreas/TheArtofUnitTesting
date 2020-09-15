import sut
import unittest
from unittest import mock

class TestSut(unittest.TestCase):
    def test_g_1(self):
        with mock.patch('sut.f') as mock_f:
            mock_f.return_value = 3
            self.assertEqual(9, sut.g(3))
    @mock.patch('sut.f')
    def test_g_2(self, mock_f):
        _list = [2, 3, 4, 5]
        for i in _list:
            mock_f.return_value = i
            self.assertEqual(i ** 2, sut.g(3))

@mock.patch('sut.f')
class TestSut2(unittest.TestCase):
    def test_g_1(self, mock_f):
        mock_f.return_value = 3
        self.assertEqual(9, sut.g(3))

    def test_g_2(self, mock_f):
        _list = [6, 7, 8]
        for i in _list:
            mock_f.return_value = i
            self.assertEqual(i ** 2, sut.g(i))

if __name__ == "__main__":
    unittest.main()
