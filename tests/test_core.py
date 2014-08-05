import unittest

from datatypes.core import filter_self_and_none


class TestValidationCore(unittest.TestCase):
    def test_can_filter_None_and_self_from_params(self):
        params = {'a': 1, 'b': '2', 'c': None, 'self': self}
        result = filter_self_and_none(params)

        self.assertFalse(None in result.itervalues(),
                         "Result should not contain None: " + repr(result))

        self.assertFalse('c' in result.iterkeys(),
                         "Result should not contain key 'c' as this is set to None: " + repr(result))

        self.assertFalse(self in result.iterkeys(), "Result should not contain key 'self': " + repr(result))
