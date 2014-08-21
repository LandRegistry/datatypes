from voluptuous import In, All
import pycountry

from datatypes.core import SingleValueValidator

valid_countries = map(lambda c: c.alpha2, pycountry.countries)

country_schema = All(str, In(valid_countries))


class IsoCountryCode(SingleValueValidator):
    def __init__(self):
        super(IsoCountryCode, self).__init__()

    def define_schema(self):
        return country_schema

    def define_error_message(self):
        return "Country must be a valid ISO country code"