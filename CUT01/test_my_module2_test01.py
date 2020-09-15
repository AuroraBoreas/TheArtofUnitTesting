import unittest
from unittest import mock
import my_module2

"""
stack as many as u can

! but ..
"""
@mock.patch('my_module2.address')
@mock.patch('my_module2.birthday')
@mock.patch('my_module2.name')
class TestHello(unittest.TestCase):
    def test_name_1(self, mock_name, mock_birthday, mock_address): # ! <~ this is shit
        mock_name.return_value = 2
        self.assertEqual(2, mock_name())

    def test_name_2(self, mock_name, mock_birthday, mock_address): # ! <~ this is shit
        mock_address.return_value = 'fuck you this shit world'
        self.assertNotEqual('hmm calm down', mock_address())

if __name__ == "__main__":
    unittest.main()