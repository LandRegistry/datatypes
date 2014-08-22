from voluptuous import MultipleInvalid, Schema
from wtforms.validators import ValidationError

from datatypes.exceptions import *


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

    def clean_input(self, dictionary):
        filtered = {}

        for k, v in dictionary.iteritems():
            if isinstance(v, dict):
                filtered[k] = self.clean_input(v)
            else:
                if v is not None:
                    filtered[k] = v

        return filtered

    def validate(self, data):
        def translate_voluptous_errors(voluptuous_exception):
            return {e.path[0]: self.error_dictionary.get(e.path[0], e.error_message)
                    for e in voluptuous_exception.errors if e.path}

        try:
            self.schema(self.clean_input(data))
        except MultipleInvalid as exception:
            raise DataDoesNotMatchSchemaException(cause=exception,
                                                  value=data,
                                                  field_errors=translate_voluptous_errors(exception))

    def define_error_dictionary(self):
        raise NoErrorDictionaryDefined()


class SingleValueValidator(Validator):
    class WtfDatatypeValidator(object):
        def __init__(self, validator, message):
            self.validator = validator
            self.message = message

        def __call__(self, form=None, field=None):
            try:
                self.validator.validate(field.data)
            except DataDoesNotMatchSchemaException as e:
                raise ValidationError(self.message if self.message else e.message)

    def __init__(self):
        super(SingleValueValidator, self).__init__()
        self.error_message = self.define_error_message()

    def wtform_validator(self, message=None):
        return SingleValueValidator.WtfDatatypeValidator(self, message)

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