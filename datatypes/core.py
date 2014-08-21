from voluptuous import MultipleInvalid, Schema

from datatypes.exceptions import *
from wtforms.validators import ValidationError


def filter_none_from_dictionary(dictionary):
    filtered = {}

    for k, v in dictionary.iteritems():
        if isinstance(v, dict):
            filtered[k] = filter_none_from_dictionary(v)
        else:
            if v is not None:
                filtered[k] = v

    return filtered


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
        def translate_voluptous_errors(voluptuous_exception):
            return {e.path[0]: self.error_dictionary.get(e.path[0], e.error_message)
                    for e in voluptuous_exception.errors if e.path}

        try:
            self.schema(self.clean_input(filter_none_from_dictionary(data)))
        except MultipleInvalid as exception:
            raise DataDoesNotMatchSchemaException(cause=exception,
                                                  value=data,
                                                  field_errors=translate_voluptous_errors(exception))

    def define_error_dictionary(self):
        raise NoErrorDictionaryDefined()


class SingleValueValidator(Validator):
    def __init__(self):
        super(SingleValueValidator, self).__init__()
        self.error_message = self.define_error_message()

    def validate_in_wtforms(self, form=None, data=None, message=None):
        try:
            self.validate(data)
        except DataDoesNotMatchSchemaException as e:
            if message is None:
                error_message = e.message
            else:
                error_message = message

            raise ValidationError(error_message)

    def validate(self, data):
        try:
            self.schema(self.clean_input(data))
        except MultipleInvalid as exception:
            raise DataDoesNotMatchSchemaException(cause=exception,
                                                  value=data,
                                                  message=self.error_message,
                                                  field_errors=self.error_message)

    def define_error_message(self):
        raise ErrorMessageNotDefined()