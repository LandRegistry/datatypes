# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes import title_validator
from datatypes.core import unicoded

dumb_entry = unicoded({
    "template" : "some text",
    "full_text" : "some text",
    "fields" : {
            "field_name_1": "something",
            "field_name_2": {"some": "other thing"}
    },
    "deeds" : [],
    "notes" : []
})

proprietorship = unicoded({
        "template" : "example text",
        "full_text" : "example text",
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
    "class_of_title": "Absolute",
    "tenure": "Freehold",
    "edition_date": "20-12-2013",
    "proprietorship": proprietorship,
    "property_description": dumb_entry,
    "price_paid": dumb_entry,
    "provisions": [],
    "easements":[],
    "restrictive_covenants" : [],
    "restrictions" : [],
    "bankruptcy" : [],
    "h_schedule": [],
    "charges" : [],
    "other" : []
})

class TestTitleValidation(unittest.TestCase):
    def test_can_validate_valid_title(self):
        try:
            title_validator.validate(simple_title)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate title: " + repr(e))

    def test_cannot_validate_title_without_required_field(self):
        for field in ["proprietorship", "property_description", "price_paid", "provisions", "easements", "restrictive_covenants", "restrictions", "bankruptcy", "charges", "other", "h_schedule"]:
            bad_title = deepcopy(simple_title)
            del bad_title[field]
            self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "%s is a required field" % field, title_validator.validate, bad_title)

    def test_cannot_validate_title_for_required_and_non_empty_fields(self):
        for field in ["class_of_title", "tenure", "title_number"]:
            bad_title = deepcopy(simple_title)
            del bad_title[field]
            self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "%s is a required field, must not be an empty string" % field, title_validator.validate, bad_title)

