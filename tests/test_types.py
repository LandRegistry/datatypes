import unittest

from datatypes.address import Address
from datatypes.core import SchemaInvalidException


class TestTypes(unittest.TestCase):
    def test_address_with_no_line_one_fails_validation(self):
        address_without_postcode = Address({
            'city': 'sometown',
            'postcode': 'AB123VC'
        })

        self.assertRaises(SchemaInvalidException, address_without_postcode.validate)

    def test_can_create_address_with_required_manadory_fields(self):
        address_with_mandatory_fields = Address({
            'line_one': '1 Accacia Avenue',
            'city': 'Somewhereville',
            'postcode': 'AB1235C'
        })

        try:
            address_with_mandatory_fields.validate
        except SchemaInvalidException:
            self.fail('Could not validate address: ' + repr(SchemaInvalidException))