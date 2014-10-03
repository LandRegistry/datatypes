# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes import title_validator
from datatypes.core import unicoded

dumb_entry = unicoded({
    "text" : "some text",
    "fields" : {
            "field_name_1": "something",
            "field_name_2": {"some": "other thing"}
    },
    "deeds" : [],
    "notes" : []
})

proprietorship = unicoded({
        "text" : "example text",
        "fields" : {"proprietors": [
                {   "name": {
                        "title" : "Balarot",
                        "full_name" : "Cheesoir",
                        "decoration" : "Elegant"
                    },
                    "address": object
                }
            ]
        },
        "deeds" : [],
        "notes": []
})

simple_title = unicoded({
    "title_number": "TEST123456789",
    "payment": {
        "price_paid": "3100.00"
    },
    "proprietorship": proprietorship,
    "property_description": dumb_entry,
    "price_paid": dumb_entry,
    "provisions": [],
    "easements":[],
    "restrictive_covenants" : [],
    "restrictions" : [],
    "bankruptcy" : []
})

class TestTitleValidation(unittest.TestCase):
    def test_can_validate_valid_title(self):
        try:
            title_validator.validate(simple_title)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate title: " + repr(e))

    def test_cannot_validate_invalid_title_number(self):
        bad_title = deepcopy(simple_title)
        del bad_title["title_number"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "title_number is a required field", title_validator.validate, bad_title)

    def test_cannot_validate_invalid_title_price_paid(self):
        bad_title = deepcopy(simple_title)
        bad_title["payment"]["price_paid"] = "£3100.00"
        self.assertRaises(DataDoesNotMatchSchemaException, title_validator.validate, bad_title)

    def test_cannot_validate_title_without_proprietorship(self):
        bad_title = deepcopy(simple_title)
        del bad_title["proprietorship"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "proprietorship is a required field", title_validator.validate, bad_title)

    def test_cannot_validate_title_without_property_description(self):
        bad_title = deepcopy(simple_title)
        del bad_title["property_description"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "property_description is a required field", title_validator.validate, bad_title)

    def test_cannot_validate_title_without_price_paid(self):
        bad_title = deepcopy(simple_title)
        del bad_title["price_paid"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "price_paid is a required field", title_validator.validate, bad_title)

    def test_cannot_validate_title_without_provisions(self):
        bad_title = deepcopy(simple_title)
        del bad_title["provisions"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "provisions is a required field", title_validator.validate, bad_title)

    def test_cannot_validate_title_without_easements(self):
        bad_title = deepcopy(simple_title)
        del bad_title["easements"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "easements is a required field", title_validator.validate, bad_title)

    def test_cannot_validate_title_without_restrictive_covenants(self):
        bad_title = deepcopy(simple_title)
        del bad_title["restrictive_covenants"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "restrictive_covenants is a required field", title_validator.validate, bad_title)

    def test_cannot_validate_title_without_restrictions(self):
        bad_title = deepcopy(simple_title)
        del bad_title["restrictions"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "restrictions is a required field", title_validator.validate, bad_title)

    def test_cannot_validate_title_without_bankruptcy(self):
        bad_title = deepcopy(simple_title)
        del bad_title["bankruptcy"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "bankruptcy is a required field", title_validator.validate, bad_title)



