import unittest

from datatypes.core import LandRegistryDatatype


class TestValidationCore(unittest.TestCase):
    def test_can_filter_none_and_self_from_params(self):
        params = {'a': 1, 'b': '2', 'c': None, 'self': self}
        result = LandRegistryDatatype._filter_none(params)

        self.assertFalse(None in result.itervalues(),
                         "Result should not contain None: " + repr(result))

        self.assertFalse('c' in result.iterkeys(),
                         "Result should not contain key 'c' as this is set to None: " + repr(result))


    def test_raises_error_if_schema_not_defined(self):
        class TestDataType(LandRegistryDatatype)