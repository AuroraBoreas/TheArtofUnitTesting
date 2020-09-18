from logan0 import LogAnalyzer
import unittest

"""
? Q: how do i do unittest w/o filesystem? 
     i wanna test my business logic only, w/o external dependencies.

* thoughts
"there is no object-oriented problem that cannot be soled by adding a layer of indirection,
except, ofc, too many layers of indirection."

You can't test sth?
add a layer that wraps up the calls to that something, and then mimic that layer in your tests.
or make that sth replaceble (so that it is itself a layer of indirection).
"""

class TestLogAnalyzer(unittest.TestCase):
    def test_isvalid_log_filename(self):
        la = LogAnalyzer()
        self.assertTrue(la.isValid_log_filename('readme.md'))


if __name__ == "__main__":
    unittest.main()