import unittest

from datatypes.address import Address
from datatypes.core import DataDoesNotMatchSchemaException


class TestTypes(unittest.TestCase):
    def setUp(self):
        self.address_with_no_fields = Address({})

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

    def test_schema_is_present_in_exception(self):
        try:
            self.address_with_no_fields.validate()
            self.fail("Should have throw exception")
        except DataDoesNotMatchSchemaException as exception:
            self.assertEqual(exception.schema, self.address_with_no_fields.schema)

    def test_can_detect_missing_fields_from_exception(self):
        try:
            self.address_with_no_fields.validate()
        except DataDoesNotMatchSchemaException as exception:
            self.assertEquals(len(exception.field_errors), 3)  # we have three required fields
