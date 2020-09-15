import unittest
from unittest import mock
import my_module3

class TestFoo(unittest.TestCase):
    def test_bar1(self):
        with mock.patch('my_module3.Foo') as mock_foo:
            # i dont see any properties inside of dir(mock_foo)
            # all attrs inside of dir(mock_foo) are "mock"
            # pprint.pprint(dir(mock_foo))
            mock_foo.bar()
            mock_foo.assret_called_with('Bob') # pass

    def test_bar2(self):
        with mock.patch('my_module3.Foo', spec=True) as mock_foo:
            # added class Foo attrs to mock obj
            mock_foo.bar()
            mock_foo.assret_called_with('Bob') # exception

if __name__ == "__main__":
    unittest.main()