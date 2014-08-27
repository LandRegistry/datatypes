import unittest

from datatypes import address_validator
from datatypes.core import DataDoesNotMatchSchemaException


class TestAddressValidation(unittest.TestCase):
    def test_address_with_no_line_one_fails_validation(self):
        address_without_postcode = {
            'city': 'sometown',
            'postcode': 'AB123VC'
        }

        self.assertRaises(DataDoesNotMatchSchemaException, address_validator.validate, address_without_postcode)

    def test_can_create_address_with_required_mandatory_fields(self):
        address_with_mandatory_fields = {
            'line_one': '1 Acacia Avenue',
            'city': 'Somewhere',
            'postcode': 'AL35PU',
            'country': 'GB'
        }

        try:
            address_validator.validate(address_with_mandatory_fields)
        except DataDoesNotMatchSchemaException as e:
            self.fail('Could not validate address: ' + repr(e))

    def test_length_of_fields_is_checked(self):
        try:
            address_validator.validate({
                'line_one': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'  # over 40 chars
            })
            self.fail("Should have thrown exception")
        except DataDoesNotMatchSchemaException as e:
            self.assertEqual(e.field_errors['line_one'],
                             'line_one is a required string field and must be a maximum of 40 characters long')

    def test_can_detect_missing_fields_from_exception(self):
        try:
            address_validator.validate({})
        except DataDoesNotMatchSchemaException as exception:
            print repr(exception.field_errors)
            self.assertEquals(len(exception.field_errors), 4)  # we have four required fields
