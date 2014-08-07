import unittest

from datatypes.address import Address
from datatypes.core import DataDoesNotMatchSchemaException


class TestTypes(unittest.TestCase):
    def test_address_with_no_line_one_fails_validation(self):
        address_without_postcode = Address({
            'city': 'sometown',
            'postcode': 'AB123VC'
        })

        self.assertRaises(DataDoesNotMatchSchemaException, address_without_postcode.validate)

    def test_can_create_address_with_required_mandatory_fields(self):
        address_with_mandatory_fields = Address({
            'line_one': '1 Acacia Avenue',
            'city': 'Somewhere',
            'postcode': 'AB1235C'
        })

        try:
            address_with_mandatory_fields.validate
        except DataDoesNotMatchSchemaException:
            self.fail('Could not validate address: ' + repr(DataDoesNotMatchSchemaException))

    def test_can_get_errors_from_validation_when_fields_are_missing(self):
        address_with_no_fields = Address({})

        self.assertRaises(DataDoesNotMatchSchemaException, address_with_no_fields.validate)
