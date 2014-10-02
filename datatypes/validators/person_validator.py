from voluptuous import Required
from datatypes.core import DictionaryValidator

person_schema = {
    Required("title"): unicode,
    Required("full_name"): unicode,
    Required("decoration"): unicode
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
