from voluptuous import All, Match
from datatypes.core import SingleValueValidator

ocg_urn_schema = Match(pattern='urn:ogc:def:crs:EPSG:\d{4,5}')


class OgcUrn(SingleValueValidator):
    def __init__(self):
        super(OgcUrn, self).__init__()

    def define_schema(self):
        return ocg_urn_schema

    def define_error_message(self):
        return "Value must be a correctly formatted OGC URN"