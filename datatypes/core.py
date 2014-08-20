from voluptuous import MultipleInvalid, Schema

from datatypes.exceptions import *
from utils import translate_voluptous_errors, filter_none_from_dictionary


class Validator(object):
    def __init__(self, required=False, extra=True):
        self.schema = Schema(schema=self.define_schema(), required=required, extra=extra)

    def clean_input(self, data):
        return data

    def define_schema(self):
        raise NoSchemaException()

    def to_canonical_form(self, data):
        return data

    def validate(self):
        raise Exception("You must define a validate method")


class DictionaryValidator(Validator):
    def __init__(self):
        super(DictionaryValidator, self).__init__()
        self.error_dictionary = self.define_error_dictionary()

    def validate(self, data):
        try:
            self.schema(self.clean_input(filter_none_from_dictionary(data)))
        except MultipleInvalid as exception:
            raise DataDoesNotMatchSchemaException(exception, translate_voluptous_errors(exception))

    def define_error_dictionary(self):
        raise NoErrorDictionaryDefined()


class SingleValueValidator(Validator):
    def __init__(self):
        super(SingleValueValidator, self).__init__()
        self.error_message = self.define_error_message()

    def validate(self, data):
        try:
            self.schema(self.clean_input(data))
        except MultipleInvalid as exception:
            raise DataDoesNotMatchSchemaException(exception, self.error_message)

    def define_error_message(self):
        raise ErrorMessageNotDefined()