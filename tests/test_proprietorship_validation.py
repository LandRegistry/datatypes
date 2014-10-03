import unittest
from copy import deepcopy

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes import proprietorship_validator
from datatypes.core import unicoded

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

class TestProprietorshipValidation(unittest.TestCase):

    def test_can_validate_valid_proprietorship(self):
        try:
            proprietorship_validator.validate(proprietorship)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate entry: " + repr(e))

    def test_cannot_validate_proprietorship_without_proprietors(self):
        invalid_proprietorship = deepcopy(proprietorship)
        del invalid_proprietorship["fields"]["proprietors"]
        try:
            proprietorship_validator.validate(invalid_proprietorship)
        except DataDoesNotMatchSchemaException as e:
            error = e.field_errors.get("fields.proprietors")
            self.assertIsNotNone(error)
            self.assertEqual("proprietors are required and there must be at least 1", error)

    def test_cannot_validate_proprietorship_with_empty_proprietors(self):
        invalid_proprietorship = deepcopy(proprietorship)
        invalid_proprietorship["fields"]["proprietors"] = []
        try:
            proprietorship_validator.validate(invalid_proprietorship)
        except DataDoesNotMatchSchemaException as e:
            error = e.field_errors.get("fields.proprietors")
            self.assertIsNotNone(error)
            self.assertEqual("proprietors are required and there must be at least 1", error)

    def test_cannot_validate_proprietorship_without_name(self):
        invalid_proprietorship = deepcopy(proprietorship)
        del invalid_proprietorship["fields"]["proprietors"][0]["name"] #ouch
        try:
            proprietorship_validator.validate(invalid_proprietorship)
        except DataDoesNotMatchSchemaException as e:
            errors = e.field_errors.get("fields.proprietors.name")
            self.assertIsNotNone(errors)
            self.assertEquals(errors, "proprietors name is required")


    def test_cannot_validate_proprietorship_without_address(self):
        invalid_proprietorship = deepcopy(proprietorship)
        del invalid_proprietorship["fields"]["proprietors"][0]["address"] #ouch
        try:
            proprietorship_validator.validate(invalid_proprietorship)
        except DataDoesNotMatchSchemaException as e:
            errors = e.field_errors.get("fields.proprietors.address")
            self.assertIsNotNone(errors)
            self.assertEquals(errors, "proprietors address is required")
