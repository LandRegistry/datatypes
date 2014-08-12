from voluptuous import MultipleInvalid
from voluptuous_errors import translate_error


def filter_none(dictionary):
    return {k: v for k, v in dictionary.iteritems() if v is not None}


class NoSchemaException(Exception):
    def __init__(self):
        super(self.__class__, self).__init__("You have not defined a schema. You must overload the 'schema' method.")


class NoErrorDictionaryDefined(Exception):
    def __init__(self):
        super(self.__class__, self).__init__("You have not defined the method error_dictionary")


class DataDoesNotMatchSchemaException(Exception):
    def __init__(self, cause, schema):
        super(self.__class__, self).__init__(cause.message + u', caused by ' + repr(cause))

        self.cause = cause
        self.schema = schema

        self.field_errors = {e.path[0]: translate_error(e.error_message)
                             for e in self.cause.errors
                             if e.path is not [] and e.path is not None}

    def __repr__(self):
        return self.__class__.__name__ + ' errors:' + repr(self.field_errors) + ' caused by:' + repr(self.cause)

    def __str__(self):
        return self.__repr__()


class Validator(object):
    def __init__(self):
        self.schema = self.schema()
        self.error_dictionary = self.error_dictionary()

    def schema(self):
        raise NoSchemaException()

    def error_dictionary(self):
        raise NoErrorDictionaryDefined()

    def to_canonical_form(self, data):
        return data

    def raise_error(self, voluptuous_exception):
        raise DataDoesNotMatchSchemaException(voluptuous_exception, self.schema)

    def validate(self, data):
        try:
            self.schema(filter_none(self.to_canonical_form(data)))
        except MultipleInvalid as voluptuousException:
            self.raise_error(voluptuousException)
