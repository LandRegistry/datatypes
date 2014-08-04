from core import LandRegistryDatatype, filter_self
from voluptuous import Schema

class Address(LandRegistryDatatype):
    def __init__(self,
                 line_one='',
                 line_two='',
                 line_three='',
                 line_four='',
                 city='',
                 country='',
                 postcode='',
                 iso_country_code=''):
        LandRegistryDatatype.__init__(self, Schema({}))
        self.store(filter_self(locals()))



