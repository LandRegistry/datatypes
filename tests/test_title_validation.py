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
    "notes" : [],
    "extra_field_to_ignore" : "should not cause validation failure"
})

proprietorship = unicoded({
        "template" : "example text",
        "full_text" : "example text",
        "fields" : {"proprietors": [
                {   "name": {
                        "title" : "Balarot",
                        "full_name" : "Cheesoir",
                        "decoration" : "Elegant",
                        "extra_field_to_ignore" : "should not cause validation failure"
                    },
                    "addresses": object
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
    "h_schedule": dumb_entry,
    "charges" : [],
    "other" : []
})

class TestTitleValidation(unittest.TestCase):
    def test_can_validate_valid_title(self):
        try:
            title_validator.validate(simple_title)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate title: " + repr(e))

    def test_can_validate_title_without_optional_fields(self):
        for field in ["price_paid", "h_schedule"]:
            title = deepcopy(simple_title)
            del title[field]
            try:
                title_validator.validate(simple_title)
            except DataDoesNotMatchSchemaException as e:
                self.fail("Could not validate title: " + repr(e))

    def test_cannot_validate_title_without_required_field(self):
        for field in ["class_of_title", "tenure", "title_number", "proprietorship", "property_description", "provisions", "easements", "restrictive_covenants", "restrictions", "bankruptcy", "charges", "other"]:
            bad_title = deepcopy(simple_title)
            del bad_title[field]
            self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "%s is a required field" % field, title_validator.validate, bad_title)

    def test_cannot_validate_title_for_required_string_fields_that_are_empty(self):
        for field in ["class_of_title", "tenure", "title_number"]:
            bad_title = deepcopy(simple_title)
            bad_title[field] = ""
            self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "%s is a required field, must not be an empty string" % field, title_validator.validate, bad_title)

    def test_cannot_validate_title_for_entry_fields_that_are_empty(self):
        for field in ["property_description", "h_schedule","price_paid"]:
            bad_title = deepcopy(simple_title)
            bad_title[field] = {} # replace dumb entry with empty object
            self.assertRaises(DataDoesNotMatchSchemaException,  title_validator.validate, bad_title)
