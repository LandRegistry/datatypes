from voluptuous import Required, In, All
from datatypes.core import DictionaryValidator
from datatypes.validators import address_validator, price_validator, geo_json_validator, entry_validator, proprietorship_validator

title_schema = {

    Required("title_number"): All(unicode),

    "extent": geo_json_validator.geo_json_schema,

    Required("proprietorship"): proprietorship_validator.proprietorship_schema,

    Required("property_description"): entry_validator.entry_schema,

    Required("price_paid"): entry_validator.entry_schema,

    Required("provisions"): [entry_validator.entry_schema],

    Required("easements"): [entry_validator.entry_schema],

    Required("restrictive_covenants"): [entry_validator.entry_schema],

    Required("restrictions"): [entry_validator.entry_schema],

    Required("bankruptcy"): [entry_validator.entry_schema],

    Required("charges"): [entry_validator.entry_schema],

    Required("other"): [entry_validator.entry_schema]

}


class Title(DictionaryValidator):
    def define_schema(self):
        return title_schema

    def define_error_dictionary(self):
        return {
            "title_number": "title_number is a required field",
            "proprietorship": "proprietorship is a required field",
            "property_description": "property_description is a required field",
            "price_paid": "price_paid is a required field",
            "provisions": "provisions is a required field",
            "easements": "easements is a required field",
            "restrictive_covenants": "restrictive_covenants is a required field",
            "restrictions": "restrictions is a required field",
            "bankruptcy": "bankruptcy is a required field"
        }
