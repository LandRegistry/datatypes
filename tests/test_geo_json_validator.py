import unittest
from datatypes.exceptions import DataDoesNotMatchSchemaException
from geojson_fixtures import *
from datatypes import geo_json_validator


class TestGeoJsonValidator(unittest.TestCase):
    def test_can_validate_geo_json(self):
        try:
            geo_json_validator.validate(sample_geojson_point)
            geo_json_validator.validate(sample_geojson_polygon)
            geo_json_validator.validate(sample_geojson_from_migration)
        except DataDoesNotMatchSchemaException as exception:
            self.fail("Should not have thrown exception " + repr(exception))

    def test_does_not_validate_invalid_geo_json(self):
        self.assertRaises(DataDoesNotMatchSchemaException, geo_json_validator.validate, sample_invalid_geojson)