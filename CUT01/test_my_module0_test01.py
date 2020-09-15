import unittest
from unittest import mock
import my_module0

class MyModuleTest(unittest.TestCase):
    """
    Two takeaways:

    ! Target Must be importable
    by default, mock will do this under the hood
    @patch('package.module.ClassName')

    still remember python import mechnism?

    ! Patch where the obj is used, NOT where the obj is created
    """
    @mock.patch('my_module0.db_write')
    def test_foo(self, mock_write):
        mock_write.return_value = 10
        x = my_module0.foo()
        self.assertEqual(x, 10)

if __name__ == "__main__":
    unittest.main()