from voluptuous import MultipleInvalid


def filter_none(params):
    return {k: v for k, v in params.iteritems() if v is not None}


class NoSchemaException(Exception):
    def __init__(self):
        super(self.__class__, self).__init__("You have not defined a schema. You must overload the 'schema' method.")


class DataDoesNotMatchSchemaException(Exception):
    def __init__(self, cause):
        super(self.__class__, self).__init__(cause.message + u', caused by ' + repr(cause))
        self.cause = cause


class LandRegistryDatatype(object):
    def __init__(self, data):
        """
        This constructor will initialise a datatype
        :param schema: The voluptuous Schema required to validate this datatype.
        """
        self.schema = self.schema()
        self.data = filter_none(self.to_canonical_form(data))

    def schema(self):
        raise NoSchemaException()

    def to_canonical_form(self, data):
        return data

    def validate(self):
        try:
            self.schema(self.data)
        except MultipleInvalid as voluptuousException:
            raise DataDoesNotMatchSchemaException(voluptuousException)
