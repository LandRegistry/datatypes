from voluptuous import MultipleInvalid, Schema

from datatypes.exceptions import *
from utils import translate_voluptous_errors, filter_none


class Validator(object):
    def __init__(self, required=False, extra=True):
        self.schema = Schema(schema=self.define_schema(), required=required, extra=extra)

    def define_schema(self):
        raise NoSchemaException()

    def to_canonical_form(self, data):
        return data

    def validate(self, data):
        try:
            self.schema(filter_none(self.to_canonical_form(data)))
        except MultipleInvalid as exception:
            raise DataDoesNotMatchSchemaException(exception, translate_voluptous_errors(exception))


class DictionaryValidator(Validator):
    def __init__(self):
        super(DictionaryValidator, self).__init__()
        self.error_dictionary = self.define_error_dictionary()

    def define_error_dictionary(self):
        raise NoErrorDictionaryDefined()


class SingleValueValidator(Validator):
    def __init__(self):
        super(SingleValueValidator, self).__init__()
        self.field_name = self.define_field_name()
        self.error_message = self.define_error_message()

    def define_field_name(self):
        raise FieldNameNotDefined()

    def define_error_message(self):
        raise ErrorMessageNotDefined()