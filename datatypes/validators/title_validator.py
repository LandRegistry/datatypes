from voluptuous import All, In
from datatypes.core import DictionaryValidator
from datatypes import address_validator, price_validator, geo_json_validator

title_schema = {
    'title_number': All(str),

    'proprietors': [
        {
            'first_name': str,
            'last_name': str
        }
    ],

    'property': {
        'address': address_validator.schema,
        'tenure': In(['freehold', 'leasehold']),
        'class-of-title': In(['absolute', 'good', 'qualified', 'possesory'])
    },

    'payment': {
        'price_paid': price_validator.schema,
        'titles': [
            str  # TODO: Check that the current title number is present here?
        ]
    },

    'extent': geo_json_validator.schema
}


class TitleValidator(DictionaryValidator):
    def define_schema(self):
        return title_schema

    def define_error_dictionary(self):
        return {

        }