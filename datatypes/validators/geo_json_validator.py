from voluptuous import Required, In, Optional, All, Length, extra
import geojson
import json

from datatypes import ogc_urn_validator
from datatypes.core import DictionaryValidator, SingleValueValidator

# This isn't intended to be a full GeoJSON validator, rather a constraining
# validator to support the types / models that the land registry have.
#
# We will also check that the GeoJSON supplied parses fully in the clean_data method
from datatypes.exceptions import DataDoesNotMatchSchemaException

geo_json_schema = {
    Required('type'): All(str, In(['Point',
                                   'MultiPoint',
                                   'LineString',
                                   'MultiLineString',
                                   'Polygon',
                                   'MultiPolygon',
                                   'GeometryCollection',
                                   'Feature',
                                   'FeatureCollection'])),

    # Currently we're only allowing named CRS
    Optional('crs'): {
        Required('type'): In(['name']),
        Required('properties'): {
            Required('name'): ogc_urn_validator.schema
        }
    },

    # These are our currently supported geometry types
    Required('geometry'): {
        Required('type'): All(str, In(['Polygon', 'MultiPolygon'])),
        Required('coordinates'): [
            [
                All(Length(min=2, max=2), [float])
            ]
        ]
    },

    Optional('properties'): {
        extra: object
    }
}


class GeoJson(DictionaryValidator):
    def define_schema(self):
        return geo_json_schema

    def define_error_dictionary(self):
        return {
            'geometry': 'A polygon or multi-polygon is required',
            'crs': "A valid 'CRS' containing an EPSG is required"
        }

    def clean_input(self, dictionary):
        try:
            geojson.loads(json.dumps(dictionary))
        except ValueError as exception:
            raise DataDoesNotMatchSchemaException(cause=exception, message='Valid GeoJSON is required')

        return dictionary


class GeoJsonString(SingleValueValidator):
    geo_dict_validator = GeoJson()

    def define_error_message(self):
        return 'Valid GeoJSON is required'

    def define_schema(self):
        return {}

    def validate(self, data):
        GeoJsonString.geo_dict_validator.validate(self.clean_input(data))

    def clean_input(self, data):
        try:
            return geojson.loads(data)
        except Exception as exception:
            raise DataDoesNotMatchSchemaException(cause=exception, message=self.error_message)


