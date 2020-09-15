"""
===
python3 documentation
===

## unittest.mock -- mock object library

unittest.mock is a library for testing in python.
it allows you to replace parts of system under test with mock objects
and make assertions about how they have been used.


## why?

unittest.mock provides a core mock class removing the need to create a host of stubs
throughout your test suite.

after performing an action, you can make assertions about which methods / attributes were used 
and arguments they were called with.

you can also specify return values and set needed attributes in the normal way.


## how?

mock is very easy to use and is designed for use with unittest.
mock is based on the 'action -> assertion' pattern 
instead of 'record -> replay' used by many mocking frameworks.

"""

import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class ProductionClass():
    pass

from unittest.mock import MagicMock
thing = ProductionClass()
thing.method = MagicMock(return_value=1)
logging.debug('{}'.format(thing.method(3, 4, 5, key='value')))
