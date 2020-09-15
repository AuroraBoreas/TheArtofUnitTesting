"""
A Magic Mock
"""
from unittest import mock
import pprint

class Foo():
    x = 20
    def bar(self):
        y = 10
        return y

def test_bar1():
    with mock.patch('__main__.Foo') as mock_foo:
        # i dont see any properties inside of dir(mock_foo)
        # all attrs inside of dir(mock_foo) are "mock"
        # pprint.pprint(dir(mock_foo))
        mock_foo.bar()
        mock_foo.assret_called_with('Bob') # exception

def test_bar2():
    with mock.patch('__main__.Foo', spec=True) as mock_foo:
        # added class Foo attrs to mock obj
        pprint.pprint(dir(mock_foo))
        mock_foo.bar()
        mock_foo.assret_called_with('Bob')




if __name__ == "__main__":
    test_bar1()
    # test_bar2()
