import unittest
from unittest import mock
import my_module2

class TestHello(unittest.TestCase):
    def setUp(self):
        mock_name = mock.patch('my_module2.name').start()
        mock_bday = mock.patch('my_module2.birthday').start()
        mock_addr = mock.patch('my_module2.address').start()
        self.addCleanup(mock.patch.stopall)
        
    def test_name_1(self):
        ...
    def test_name_2(self):
        ...

if __name__ == "__main__":
    unittest.main()