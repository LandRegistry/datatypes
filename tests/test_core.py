import unittest
from voluptuous import All, Length

from datatypes.core import DictionaryValidator, filter_none_from_dictionary, SingleValueValidator
from datatypes.exceptions import *
from wtforms.validators import ValidationError


class TestValidationCore(unittest.TestCase):
    def test_can_filter_none_and_self_from_dictionary(self):
        dictionary = {'a': 1, 'b': '2', 'c': None, 'self': self}
        result = filter_none_from_dictionary(dictionary)

        self.assertFalse(None in result.itervalues(),
                         "Result should not contain None: " + repr(result))

        self.assertFalse('c' in result.iterkeys(),
                         "Result should not contain key 'c' as this is set to None: " + repr(result))

    def test_can_filter_none_from_nested_dictionary(self):
        dictionary = {'a': None, 'b': {'c': None, 'd': 'd'}}
        result = filter_none_from_dictionary(dictionary)

        self.assertFalse('a' in result.iterkeys())
        sub_dictionary = result['b']
        self.assertFalse('c' in sub_dictionary.iterkeys())

    def test_single_value_validator_raises_correct_error_messages(self):
        class TestDatType(SingleValueValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def define_schema(self):
                return All(Length(max=3))

            def define_error_message(self):
                return "foo"

        try:
            TestDatType().validate("1234")
            self.fail("Should have throw exception")
        except DataDoesNotMatchSchemaException as exception:
            self.assertEqual(exception.message, "foo")

    def test_raises_error_if_schema_not_defined(self):
        class TestDataType(DictionaryValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def define_error_dictionary(self):
                pass

        self.assertRaises(NoSchemaException, TestDataType)

    def test_raises_error_if_error_message_not_defined(self):
        class TestDataType(SingleValueValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def define_schema(self):
                pass

        self.assertRaises(ErrorMessageNotDefined, TestDataType)

    def test_raises_error_if_error_dictionary_is_not_defined(self):
        class TestDataType(DictionaryValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def define_schema(self):
                pass

        self.assertRaises(NoErrorDictionaryDefined, TestDataType)

    def test_can_validate_single_value_in_wtforms(self):
        class TestDataType(SingleValueValidator):
            def __init__(self):
                super(self.__class__, self).__init__()

            def define_schema(self):
                return All(str, Length(max=3))

            def define_error_message(self):
                return "egg"

        validator = TestDataType()

        try:
            validator.validate_in_wtforms(data="1234", message="sausages")
            self.fail("Should have thrown an exception")
        except ValidationError as exception:
            self.assertEqual(exception.message, "sausages")

        try:
            validator.validate_in_wtforms(data="1234")
            self.fail("Should have thrown exception")
        except ValidationError as exception:
            self.assertEqual(exception.message, "egg")
