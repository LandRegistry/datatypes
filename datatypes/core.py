from voluptuous import Schema


def filter_self(params):
    """
    Take a map of parameters & values (usually got by running local() in the current method)
    and filter the parameter named 'self' from this list.
    This is used so that we can define constructors that take named parameters and use
    them to drive the model.
    :param params: a map of k=>v of method arguments
    :return: map with self removed
    """
    print locals()
    return {k: v for k, v in params.items() if k is not 'self'}


class LandRegistryDatatype(object):
    def __init__(self, schema):
        """
        This constructor will initialise a datatype
        :param schema: The voluptuous schema required to validate this datatype.
        """
        self.data = ()
        self.schema = schema

    def store(self, data):
        self.data = self.to_canonical_form(data)

    def to_canonical_form(self, data):
        return data


