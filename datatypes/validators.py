from datatypes.core import Validator
from datatypes import schemas


class AddressValidator(Validator):
    def __init__(self):
        super(self.__class__, self).__init__()

    def schema(self):
        return schemas.address_schema

    def error_dictionary(self):
        return {

        }