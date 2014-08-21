from voluptuous import Required, In, Optional, All, Coerce
from datatypes.core import DictionaryValidator
from datatypes import ogc_urn_validator


geo_json_schema = {
    Required('type'): In("Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon",
                         "GeometryCollection", "Feature", "FeatureCollection"),

    # Currently we're only allowing named CRS
    Optional('crs'): {
        Required('type'): All(Coerce(str)), # should be 'name'
        Required('properties') : {
            Required('name') : ogc_urn_validator.schema
        }
    }
}


class GeoJson(DictionaryValidator):
    def define_schema(self):
        return geo_json_schema

    def define_error_dictionary(self):
        return {

        }
