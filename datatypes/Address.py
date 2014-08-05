from voluptuous import Schema

from datatypes.core import LandRegistryDatatype


class Address(LandRegistryDatatype):
    def __init__(self, data):
        super(self.__class__, self).__init__(data)

    def schema(self):
        return Schema({

        })