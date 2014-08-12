import unittest

from datatypes.core import DictionaryValidator, filter_none, SingleValueValidator
from datatypes.exceptions import *


class TestValidationCore(unittest.TestCase):
    def test_can_filter_none_and_self_from_params(self):
        params = {'a': 1, 'b': '2', 'c': None, 'self': self}
        result = filter_none(params)

        self.assertFalse(None in result.itervalues(),
                         "Result should not contain None: " + repr(result))

        self.assertFalse('c' in result.iterkeys(),
                         "Result should not contain key 'c' as this is set to None: " + repr(result))

    def test_raises_error_if_schema_not_defined(self):
        class TestDataType(DictionaryValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def error_dictionary(self):
                pass

        self.assertRaises(NoSchemaException, TestDataType)

    def test_raises_error_if_fieldname_is_not_defined(self):
        class TestDataType(SingleValueValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def schema(self):
                pass

            def error_message(self):
                pass

        self.assertRaises(FieldNameNotDefined, TestDataType)

    def test_raises_error_if_error_message_not_defined(self):
        class TestDataType(SingleValueValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def schema(self):
                pass

            def field_name(self):
                pass

        self.assertRaises(ErrorMessageNotDefined, TestDataType)

    def test_raises_error_if_error_dictionary_is_not_defined(self):
        class TestDataType(DictionaryValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def schema(self):
                pass

        self.assertRaises(NoErrorDictionaryDefined, TestDataType)


