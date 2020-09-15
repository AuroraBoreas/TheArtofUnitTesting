import unittest
from unittest import mock
import my_module4

class TestBar(unittest.TestCase):
    @mock.patch('my_module4.foo', spec=True)
    def test_bar(self, mock_foo):
        # mock_foo.return_value = None
        my_module4.bar() # pass

if __name__ == "__main__":
    unittest.main()