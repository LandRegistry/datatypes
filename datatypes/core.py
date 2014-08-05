class LandRegistryDatatype(object):
    def __init__(self, data):
        """
        This constructor will initialise a datatype
        :param schema: The voluptuous Schema required to validate this datatype.
        """
        self.schema = self.schema()
        self.store(LandRegistryDatatype._filter_none(data))

    def store(self, data):
        self.data = self.to_canonical_form(data)

    def schema(self):
        raise Exception("You need to override method schema() and return a Schema for validation")

    def to_canonical_form(self, data):
        return data

    def is_valid(self):
        return self.schema(self.data)

    @staticmethod
    def _filter_none(params):
        return {k: v
                for k, v in params.iteritems()
                if v is not None}
