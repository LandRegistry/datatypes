import unittest
from copy import deepcopy

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes import deed_validator
from datatypes.core import unicoded

people = unicoded([ { "title" : "Mrs",
            "full_name": "Bootata Smick",
            "decoration": ""
        },
        {   "title" : "Mr",
            "full_name": "Mishmisha Okasha",
            "decoration": ""
        }
])

deed =  unicoded({
    "type" : "Transfer",
    "date": "01.06.1996",
    "parties": people
})

class TestDeedValidation(unittest.TestCase):

    def test_can_validate_valid_deed(self):
        try:
            deed_validator.validate(deed)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate deed: " + repr(e))

    def test_does_not_validate_deed_without_type(self):
        invalid_deed = deepcopy(deed)
        del invalid_deed["type"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "type is a required field", deed_validator.validate, invalid_deed)

    def test_does_not_validate_deed_without_date(self):
        invalid_deed = deepcopy(deed)
        del invalid_deed["date"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "date is a required field", deed_validator.validate, invalid_deed)

    def test_does_not_validate_deed_without_parties(self):
        invalid_deed = deepcopy(deed)
        del invalid_deed["parties"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "at least two parties are required", deed_validator.validate, invalid_deed)

    def test_does_not_validate_deed_without_at_least_two_parties(self):
        invalid_deed = deepcopy(deed)
        invalid_deed["parties"] = [people[0]]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "at least two parties are required", deed_validator.validate, invalid_deed)


