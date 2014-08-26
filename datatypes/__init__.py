from datatypes.validators.iso_country_code_validator import IsoCountryCode
from datatypes.validators.ogc_urn_validator import OgcUrn
from datatypes.validators.postcode_validator import Postcode
from datatypes.validators.price_validator import Price
from datatypes.validators.address_validator import Address

price_validator = Price()
address_validator = Address()
postcode_validator = Postcode()
country_code_validator = IsoCountryCode()
ogc_urn_validator = OgcUrn()

from datatypes.validators.geo_json_validator import GeoJson, GeoJsonString

geo_json_validator = GeoJson()
geo_json_string_validator = GeoJsonString()