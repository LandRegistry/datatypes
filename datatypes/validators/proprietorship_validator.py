from voluptuous import Required, All, Length
from datatypes.core import DictionaryValidator

from datatypes.validators import deed_validator
from datatypes.validators import person_validator

proprietorship_schema = {
    Required("text"): All(str),
    Required("fields"): {
        Required("proprietors"): All( Length(min=1),
            [ { Required("name"): person_validator.person_schema,
                Required("address"): object  # TBC - settle on address format!
              }
            ])
    },
    Required("deeds"): [deed_validator.deed_schema],
    Required("notes"): []
}

class Proprietorship(DictionaryValidator):
    def define_schema(self):
        return proprietorship_schema

    def define_error_dictionary(self):
        return {
            "text": "text is a required field",
            "fields": "fields are required",
            "fields.proprietors": "proprietors are required and there must be at least 1",
            "fields.proprietors.name": "proprietors name is required",
            "fields.proprietors.address": "proprietors address is required",
            "deeds": "deeds are required",
            "notes": "notes are required"
        }
