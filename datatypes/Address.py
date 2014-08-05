from voluptuous import Schema, Required, Optional

from datatypes.core import LandRegistryDatatype


class Address(LandRegistryDatatype):
    def __init__(self, addressData):
        super(self.__class__, self).__init__(addressData)

    def schema(self):
        return Schema({
            Required('line_one'): str,
            Optional('line_two'): str,
            Optional('line_three'): str,
            Optional('line_four'): str,
            Required('city'): str,
            Required('postcode'): str
        })