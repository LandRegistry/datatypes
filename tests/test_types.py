import unittest

from datatypes.address import Address


class TestTypes(unittest.TestCase):
    def test_can_validate_address_structure(self):
        address_without_postcode = Address({
            'line_one': '1 Accacia avenue',
            'city': 'sometown'
        })

        self.assertFalse(address_without_postcode.is_valid(), "Address without postcode should not be valid")
