from voluptuous import Schema

from datatypes.core import LandRegistryDatatype


class Address(LandRegistryDatatype):
    def __init__(self, addressData):
        super(self.__class__, self).__init__(addressData)

    def schema(self):
        return Schema({

        })