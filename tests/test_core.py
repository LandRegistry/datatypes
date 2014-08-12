import unittest

from datatypes.core import Validator, filter_none, NoSchemaException, NoErrorDictionaryDefined


class TestValidationCore(unittest.TestCase):
    def test_can_filter_none_and_self_from_params(self):
        params = {'a': 1, 'b': '2', 'c': None, 'self': self}
        result = filter_none(params)

        self.assertFalse(None in result.itervalues(),
                         "Result should not contain None: " + repr(result))

        self.assertFalse('c' in result.iterkeys(),
                         "Result should not contain key 'c' as this is set to None: " + repr(result))

    def test_raises_error_if_schema_not_defined(self):
        class TestDataType(Validator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def error_dictionary(self):
                pass

        self.assertRaises(NoSchemaException, TestDataType)

    def test_raises_error_if_error_dictionary_is_not_defined(self):
        class TestDataType(Validator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def schema(self):
                pass

        self.assertRaises(NoErrorDictionaryDefined, TestDataType)


