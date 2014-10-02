import unittest
from copy import deepcopy

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes import person_validator
from datatypes.core import str_to_uni_dict

person =  str_to_uni_dict({
    "title" : "Mrs",
    "full_name": "Bootata Smick",
    "decoration": ""
})

class TestPersonValidation(unittest.TestCase):

    def test_can_validate_valid_person(self):
        try:
            person_validator.validate(person)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate person: " + repr(e))

    def test_does_not_validate_person_without_title(self):
        invalid_person = deepcopy(person)
        del invalid_person["title"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "title is a required field", person_validator.validate, invalid_person)

    def test_does_not_validate_person_without_full_name(self):
        invalid_person = deepcopy(person)
        del invalid_person["full_name"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "full_name is a required field", person_validator.validate, invalid_person)

    def test_does_not_validate_person_without_decoration(self):
        invalid_person = deepcopy(person)
        del invalid_person["decoration"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "decoration is a required field", person_validator.validate, invalid_person)
