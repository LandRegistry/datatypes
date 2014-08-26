import unittest
from datatypes.exceptions import DataDoesNotMatchSchemaException
from geojson_fixtures import sample_geojson_point, sample_geojson_polygon, sample_geojson_from_migration
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
        invalid_geo_json = {'foo': 'bar'}
        self.assertRaises(DataDoesNotMatchSchemaException, geo_json_validator.validate, invalid_geo_json)
        