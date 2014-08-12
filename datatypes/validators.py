from datatypes.core import Validator
from datatypes.schemas import address_schema


class AddressValidator(Validator):
    def __init__(self, address_data):
        super(self.__class__, self).__init__(address_data)

    def schema(self):
        return address_schema

    def error_dictionary(self):
        return {
            
        }