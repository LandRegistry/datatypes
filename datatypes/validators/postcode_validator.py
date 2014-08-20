from voluptuous import All
from datatypes.core import SingleValueValidator

postcode_schema = All(str)


class Postcode(SingleValueValidator):
    def __init__(self):
        super(Postcode, self).__init__()

    def define_schema(self):
        return postcode_schema


    def define_error_message(self):
        return {

        }