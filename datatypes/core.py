def filter_none(params):
    return {k: v for k, v in params.iteritems() if v is not None}


class NoSchemaException(Exception):
    pass


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

    def is_valid(self):
        return self.schema(self.data)

