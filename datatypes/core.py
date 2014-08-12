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

    def validate(self, data):
        try:
            self.schema(filter_none(self.to_canonical_form(data)))
        except MultipleInvalid as voluptuous_exception:
            field_errors = {e.path[0]: translate_error(e.error_message)
                            for e in voluptuous_exception.errors
                            if e.path is not [] and e.path is not None}
            raise DataDoesNotMatchSchemaException(voluptuous_exception, field_errors)


class DictionaryValidator(Validator):
    def __init__(self):
        super(DictionaryValidator, self).__init__()
        self.error_dictionary = self.error_dictionary()

    def error_dictionary(self):
        raise NoErrorDictionaryDefined()


class SingleValueValidator(Validator):
    def __init__(self):
        super(SingleValueValidator, self).__init__()
        self.field_name = self.field_name()
        self.error_message = self.error_message()

    def field_name(self):
        raise FieldNameNotDefined()

    def error_message(self):
        raise ErrorMessageNotDefined()