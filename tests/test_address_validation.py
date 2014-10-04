import unittest

from copy import deepcopy
from datatypes import address_validator
from datatypes.core import DataDoesNotMatchSchemaException


class TestAddressValidation(unittest.TestCase):

    def setUp(self):

        self.address_with_mandatory_fields = {
            u"full_address" : u"8 Acacia Avenue, Bootata, AL35PU",
            u"house_no" : u"8",
            u"street_name" : u"Acacia Avenue",
            u"town" : u"Bootata",
            u"postal_county" : u"",
            u"region_name" : u"Smotania",
            u"postcode" : u"AL35PU",
            u"country" : u"Wales"
        }

        self.no_full_address = {
            u"house_no" : u"8",
            u"street_name" : u"Acacia Avenue",
            u"town" : u"Bootata",
            u"postal_county" : u"",
            u"region_name" : u"Smotania",
            u"postcode" : u"AL35PU",
            u"country": u"Wales"
        }

        self.without_all_additional_fields = {
            u"full_address" : u"8 Acacia Avenue, Bootata, AL35PU"
        }


    def test_address_with_no_full_address_fails_validation(self):
        self.assertRaises(DataDoesNotMatchSchemaException, address_validator.validate, self.no_full_address)

    def test_address_without_additional_fields_fails_validation(self):
        self.assertRaises(DataDoesNotMatchSchemaException, address_validator.validate, self.without_all_additional_fields)

    def test_address_with_whitespace_full_address_fails_validation(self):
        address_with_whitespace_full_address = deepcopy(self.address_with_mandatory_fields )
        address_with_whitespace_full_address["full_address"] = "    \t \n  "
        self.assertRaises(DataDoesNotMatchSchemaException, address_validator.validate, address_with_whitespace_full_address)

    def test_can_create_address_with_required_mandatory_fields(self):
        try:
            address_validator.validate(self.address_with_mandatory_fields)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate address: " + repr(e))

    def test_can_detect_correct_number_of_missing_fields_from_exception(self):
        try:
            address_validator.validate({})
        except DataDoesNotMatchSchemaException as exception:
            print repr(exception.field_errors)
            self.assertEquals(len(exception.field_errors), 8)  # we have eight required fields
