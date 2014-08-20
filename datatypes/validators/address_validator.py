from voluptuous import Required, Optional, All, Length
from datatypes.core import DictionaryValidator
from datatypes.validators import postcode_validator, iso_country_code_validator

address_schema = {
    Required('line_one'): All(str, Length(max=40)),
    Optional('line_two'): All(str, Length(max=40)),
    Optional('line_three'): All(str, Length(max=40)),
    Optional('line_four'): All(str, Length(max=40)),
    Required('city'): All(str, Length(max=40)),
    Required('postcode'): postcode_validator.postcode_schema,
    Required('country'): iso_country_code_validator.country_schema
}


class Address(DictionaryValidator):
    def __init__(self):
        super(Address, self).__init__()

    def define_schema(self):
        return address_schema

    def define_error_dictionary(self):
        return {

        }