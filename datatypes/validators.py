from voluptuous import Required, All, Length, Optional

from datatypes.core import DictionaryValidator, SingleValueValidator


class AddressValidator(DictionaryValidator):
    def __init__(self):
        super(AddressValidator, self).__init__()

    def define_schema(self):
        return {
            Required('line_one'): All(str, Length(max=40)),
            Optional('line_two'): All(str, Length(max=40)),
            Optional('line_three'): All(str, Length(max=40)),
            Optional('line_four'): All(str, Length(max=40)),
            Required('city'): All(str, Length(max=40)),
            Required('postcode'): PostcodeValidator.define_schema
        }

    def define_error_dictionary(self):
        return {

        }


class PostcodeValidator(SingleValueValidator):
    def __init__(self):
        super(PostcodeValidator, self).__init__()

    def define_schema(self):
        return All(str)


    def define_error_message(self):
        return {

        }