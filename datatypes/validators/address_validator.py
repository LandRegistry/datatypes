from voluptuous import Required, Optional, All, Length, Coerce
from datatypes.core import DictionaryValidator
from datatypes.validators import postcode_validator, iso_country_code_validator

address_schema = {
    Required('line_one'): All(Coerce(unicode), Length(max=40)),
    Optional('line_two'): All(unicode, Length(max=40)),
    Optional('line_three'): All(unicode, Length(max=40)),
    Optional('line_four'): All(unicode, Length(max=40)),
    Required('city'): All(unicode, Length(max=40)),
    Required('postcode'): postcode_validator.postcode_schema,
    Required('country'): iso_country_code_validator.country_schema
}


class Address(DictionaryValidator):
    def define_schema(self):
        return address_schema

    def define_error_dictionary(self):
        return {
            'line_one': 'line_one is a required unicode field and must be a maximum of 40 characters long',
            'line_two': 'line_two must be a unicode which is a maximum of 40 characters long',
            'line_three': 'line_three must be a unicode which is a maximum of 40 characters long',
            'line_four': 'line_four must be a unicode which is a maximum of 40 characters long',
            'city': 'city is a required unicode field and must be a maximum of 40 characters long',
            'postcode': 'postcode must be a valid UK postcode',
            'country': 'country must be a valid ISO 2 letter country code'
        }
