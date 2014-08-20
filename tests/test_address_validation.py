import unittest

from datatypes.validators.address_validator import Address
from datatypes.core import DataDoesNotMatchSchemaException


class TestAddressValidation(unittest.TestCase):
    def setUp(self):
        self.address_validator = Address()

    def test_address_with_no_line_one_fails_validation(self):
        address_without_postcode = {
            'city': 'sometown',
            'postcode': 'AB123VC'
        }

        self.assertRaises(DataDoesNotMatchSchemaException, self.address_validator.validate, address_without_postcode)

    def test_can_create_address_with_required_mandatory_fields(self):
        address_with_mandatory_fields = {
            'line_one': '1 Acacia Avenue',
            'city': 'Somewhere',
            'postcode': 'AB1235C',
            'country': 'GB'
        }

        try:
            self.address_validator.validate(address_with_mandatory_fields)
        except DataDoesNotMatchSchemaException:
            self.fail('Could not validate address: ' + repr(DataDoesNotMatchSchemaException))

    def test_can_detect_missing_fields_from_exception(self):
        try:
            self.address_validator.validate({})
        except DataDoesNotMatchSchemaException as exception:
            print repr(exception.field_errors)
            self.assertEquals(len(exception.field_errors), 4)  # we have three required fields
