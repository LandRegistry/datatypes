from voluptuous import MultipleInvalid, Schema
from datatypes.exceptions import *


def filter_none(dictionary):
    return {k: v for k, v in dictionary.iteritems() if v is not None}


class Validator(object):
    def __init__(self, required=False, extra=True):
        self.schema = Schema(schema=self.schema(), required=required, extra=extra)

    def schema(self):
        raise NoSchemaException()

    def to_canonical_form(self, data):
        return data

    def raise_error(self, voluptuous_exception):
        raise DataDoesNotMatchSchemaException(voluptuous_exception)

    def validate(self, data):
        try:
            self.schema(filter_none(self.to_canonical_form(data)))
        except MultipleInvalid as voluptuousException:
            self.raise_error(voluptuousException)


class DictionaryValidator(Validator):
    def __init__(self):
        super(DictionaryValidator, self).__init__()
        self.error_dictionary = self.error_dictionary()

    def error_dictionary(self):
        raise NoErrorDictionaryDefined()


class SingleValueValidator(Validator):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.error_dictionary = self.error_dictionary()
        self.field_name = self.field_name()
        self.error_message = self.error_message()

    def field_name(self):
        raise FieldNameNotDefined()

    def error_message(self):
        raise