from voluptuous import Required, All, Optional
from datatypes.core import DictionaryValidator

person_schema = {
    Required("title"): str,
    Required("full_name"): str,
    Required("decoration"): str
}

class Person(DictionaryValidator):

    def define_schema(self):
        return person_schema

    def define_error_dictionary(self):
        return {
            "title": "title is a required field",
            "full_name": "full_name is a required field",
            "decoration": "decoration is a required field"
        }
