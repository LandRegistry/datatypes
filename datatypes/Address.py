from voluptuous import Schema, Required, Optional, All, Length

from datatypes.core import LandRegistryDatatype


class Address(LandRegistryDatatype):
    def __init__(self, addressData):
        super(self.__class__, self).__init__(addressData)

    def schema(self):
        return Schema({
            Required('line_one'): {str: All(Length(max=40))},
            Optional('line_two'): {str: All(Length(max=40))},
            Optional('line_three'): {str: All(Length(max=40))},
            Optional('line_four'): {str: All(Length(max=40))},
            Required('city'): {str: All(Length(max=40))},
            Required('postcode'): str
        })
