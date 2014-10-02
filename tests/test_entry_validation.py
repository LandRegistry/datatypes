import unittest
from copy import deepcopy

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes import entry_validator
from datatypes.core import str_to_uni_dict

deeds =  str_to_uni_dict([{
    "type" : "Transfer",
    "date": "01.06.1996",
    "parties": [ { "title" : "Mrs",
                 "full_name": "Bootata Smick",
                 "decoration": ""
              },
                { "title" : "Mr",
                "full_name": "Mishmisha Okasha",
              "decoration": ""
              }
        ]
}])

entry = str_to_uni_dict({
        "text" : "example text",
        "fields" : {"field1" : "value1",
                    "field2" : "value2",
                    "fieldN" : {"object_field": "object_value"}},

        "deeds" : [],
        "notes": []
})

class TestEntryValidation(unittest.TestCase):

    def test_can_validate_valid_entry_with_empty_deeds_and_notes(self):
        try:
            entry_validator.validate(entry)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate entry: " + repr(e))

    def test_can_validate_valid_entry_with_deeds_added(self):
        try:
            entry["deeds"] = deeds
            entry_validator.validate(entry)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate entry: " + repr(e))

    def test_does_not_validate_entry_without_text(self):
        invalid_entry = str_to_uni_dict(deepcopy(entry))
        del invalid_entry["text"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "text is a required field", entry_validator.validate, invalid_entry)

    def test_does_not_validate_entry_without_fields(self):
        invalid_entry = str_to_uni_dict(deepcopy(entry))
        del invalid_entry["fields"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "fields are required", entry_validator.validate, invalid_entry)

    def test_does_not_validate_entry_without_deeds(self):
        invalid_entry = str_to_uni_dict(deepcopy(entry))
        del invalid_entry["deeds"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "deeds are required", entry_validator.validate, invalid_entry)

    def test_does_not_validate_entry_without_notes(self):
        invalid_entry = str_to_uni_dict(deepcopy(entry))
        del invalid_entry["notes"]
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, "notes are required", entry_validator.validate, invalid_entry)




