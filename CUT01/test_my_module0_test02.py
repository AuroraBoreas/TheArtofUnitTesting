import unittest
from unittest import mock
import my_module0

class TestFoo(unittest.TestCase):
    def test_foo(self):
        with mock.patch('my_module0.db_write') as mock_write:
            # shoud PASS
            mock_write.return_value = 10
            x = my_module0.foo()
            self.assertEqual(x, 10)
        # ! should NOT pass
        y = my_module0.foo()
        self.assertEqual(y, 5)

if __name__ == "__main__":
    unittest.main()