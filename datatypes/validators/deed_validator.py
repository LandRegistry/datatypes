from voluptuous import Required, All, Length
from datatypes.core import DictionaryValidator

deed_schema = {
    Required("type"): All(unicode),
    Required("date"):  All(unicode),
    Required("parties"): All(Length(min=2), [ object] , extra=True)
}

class Deed(DictionaryValidator):

    def define_schema(self):
        return deed_schema

    def define_error_dictionary(self):
        return {
            "type": "type is a required field",
            "date": "date is a required field",
            "parties": "at least two parties are required"
        }
