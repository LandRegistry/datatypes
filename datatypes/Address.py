from core import LandRegistryDatatype, filter_self_and_none
from voluptuous import Schema


class Address(LandRegistryDatatype):
    def __init__(self,
                 line_one=None,
                 line_two=None,
                 line_three=None,
                 line_four=None,
                 city=None,
                 country=None,
                 postcode=None,
                 iso_country_code=None):
        LandRegistryDatatype.__init__(self)
        self.store(filter_self_and_none(locals()))

    def schema(self):
        return Schema({

        })