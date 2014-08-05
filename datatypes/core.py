def filter_self_and_none(params):
    """
    Take a map of parameters & values (usually got by running locals() in the current method)
    and filter the parameter named 'self' from this list.
    This is used so that we can define constructors that take named parameters and use
    them to drive the model.
    :param params: a map of k=>v of method arguments
    :return: map with self removed
    """
    return {k: v
            for k, v in params.iteritems()
            if v is not None and k is not 'self'}


class LandRegistryDatatype(object):
    def __init__(self):
        """
        This constructor will initialise a datatype
        :param schema: The voluptuous Schema required to validate this datatype.
        """
        self.data = ()
        self.schema = self.schema()

    def store(self, data):
        self.data = self.to_canonical_form(data)

    def schema(self):
        raise Exception("You need to override method schema() and return a Schema for validation")

    def to_canonical_form(self, data):
        return data

    def is_valid(self):
        return self.schema(self.data)
