import unittest
from unittest import mock

@mock.patch('my_module0.db_write')
class TestFoo(unittest.TestCase):
    def test_foo_1(self, mock_write):
        ...

    def test_foo_2(self, mock_write):
        ...


if __name__ == "__main__":
    unittest.main()