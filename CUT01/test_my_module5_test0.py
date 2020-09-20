from my_module5 import foo, bar
import unittest
from unittest import mock

class TestMyModdule(unittest.TestCase):
    def setUp(self):
        self.f = foo()
        self.mock_name = mock.patch('my_module5.foo.name').start()
        self.mock_bday = mock.patch('my_module5.foo.birthday').start()
        self.mock_addr = mock.patch('my_module5.foo.address').start()
        self.addCleanup(mock.patch.stopall)
        # or one by one, do w/e u want
        # self.addCleanup(self.mock_name.stop)
    
    def test_name(self):
        self.assertEqual(self.mock_name, self.f.name)
    def test_bday(self):
        self.assertEqual(self.mock_bday, self.f.birthday)
    def test_addr(self):
        self.assertEqual(self.mock_addr, self.f.address)


if __name__ == "__main__":
    """the test shows class attributes are same as instance's attributes.

    ? what the difference btwn class Fields/attributes/properties?
    link: https://stackoverflow.com/questions/16751269/oop-terminology-class-attribute-property-field-data-member
    
    @millimoose:
    "Fields", "class variables", and "attributes" are more-or-less the same 
    - a low-level storage slot attached to an object. 
    
    Each language's documentation might use a different term consistently, 
    but most actual programmers use them interchangeably. 

    (However, this also means some of the terms can be ambiguous, 
    like "class variable" - which can be interpreted as "a variable of an instance of a given class", 
    or "a variable of the class object itself" in a language 
    where class objects are something you can manipulate directly.)

    also
    
    Properties expose fields.
    Fields should (almost always) be kept private to a class and accessed via get and set properties. 
    
    Properties provide a level of abstraction allowing you to change the fields 
    while not affecting the external way they are accessed by the things that use your class.
    
    """
    unittest.main()