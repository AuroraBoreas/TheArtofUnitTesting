import unittest
from unittest import mock


class TestFoo(unittest.TestCase):
    @mock.patch('my_module0.db_write')
    def test_foo_1(self, mock_write):
        ...
    
    def test_foo_2(self):
        ...


if __name__ == "__main__":
    unittest.main()