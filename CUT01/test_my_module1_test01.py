import unittest
from unittest import mock
import my_module1

class MyModuleTest(unittest.TestCase):
    """
    scope matters
    +-----------------------------------------+
    |       class decorator                   |
    |  +----------------------------------+   |
    |  |    function decorator            |   |
    |  |  +----------------------------+  |   |
    |  |  |      context manager       |  |   | start / stop
    |  |  |                            |  |   |
    |  |  |                            |  |   |
    |  |  |                            |  |   |
    |  |  +----------------------------+  |   |
    |  |                                  |   |
    |  +----------------------------------+   |
    |                                         |
    +-----------------------------------------+

    """
    @mock.patch('my_module1.db_write')
    def test_foo(self, mock_write):
        mock_write.return_value = 10
        x = my_module1.foo()
        self.assertEqual(x, 10)

if __name__ == "__main__":
    unittest.main()