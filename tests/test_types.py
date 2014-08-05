import unittest

from datatypes.address import Address
from datatypes.core import SchemaInvalidException


class TestTypes(unittest.TestCase):
    def test_address_with_no_line_one_fails_validation(self):
        address_without_postcode = Address(
            {
                'city': 'sometown',
                'postcode': 'AB123VC'
            }
        )

        self.assertRaises(SchemaInvalidException, address_without_postcode.validate)
