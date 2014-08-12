from datatypes.core import DictionaryValidator, SingleValueValidator
from datatypes import schemas


class AddressValidator(DictionaryValidator):
    def __init__(self):
        super(self.__class__, self).__init__()

    def schema(self):
        return schemas.address_schema

    def error_dictionary(self):
        return {

        }


class PostcodeValidator(SingleValueValidator):
    def __init__(self):
        super(self.__class__, self).__init__()

    def schema(self):
        return schemas.postcode_schema

    def error_dictionary(self):
        return {

        }