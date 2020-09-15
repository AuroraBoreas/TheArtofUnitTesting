"""
===============
The Argument
===============

Mock Problems

1. misspelled assert look like attributes

mock_foo.assret_called_with()

2. mocked obj called incorrectly pass silently

def foo(name):
    return "hello {}".format(name)
def bar():
    print(foo())



======
kwargs
======

@patch('my_module.Foo.name', return_value='ZL')
@patch('my_module.Foo', name='ZL', month='June')
@patch('my_module.Foo', **{'name.return_value': 'Lisa'})


"""