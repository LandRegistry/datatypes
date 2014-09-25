from voluptuous import Required, In, Optional, All, Length, Coerce
from datatypes.core import DictionaryValidator
from datatypes.validators import address_validator, price_validator, geo_json_validator, entry_validator

title_schema = {
    Required("title_number"): All(str),

    "proprietors": [
        {
            "full_name": str
        }
    ],

    "property": {
        "address": address_validator.address_schema,
        "tenure": In(["freehold", "leasehold"]),
        "class-of-title": In(["absolute", "good", "qualified", "possesory"])
    },

    Required("payment"): {
        Required("price_paid"): price_validator.price_schema,
        "titles": [
            str  # TODO: Check that the current title number is present here?
        ]
    },

    "extent": geo_json_validator.geo_json_schema,

    Required("proprietorship"): entry_validator.entry_schema,

    Required("property_description"): entry_validator.entry_schema,

    Required("price_paid"): entry_validator.entry_schema,

    Required("provisions"): [entry_validator.entry_schema],

    Required("easements"): [entry_validator.entry_schema],

    Required("restrictive_covenants"): [entry_validator.entry_schema],

    Required("restrictions"): [entry_validator.entry_schema],

    Required("bankruptcy"): [entry_validator.entry_schema]
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
