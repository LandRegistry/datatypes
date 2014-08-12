from datatypes.core import DictionaryValidator, SingleValueValidator
from datatypes import schemas


class AddressValidator(DictionaryValidator):
    def __init__(self):
        super(AddressValidator, self).__init__()

    def schema(self):
        return schemas.address_schema

    def error_dictionary(self):
        return {

        }


class PostcodeValidator(SingleValueValidator):
    def __init__(self):
        super(PostcodeValidator, self).__init__()

    def schema(self):
        return schemas.postcode_schema

    def error_dictionary(self):
        return {

        }