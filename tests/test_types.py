import unittest

from datatypes.address import Address


class TestTypes(unittest.TestCase):
    def test_can_validate_address_structure(self):
        address = Address(line_one = "foo")
        print address.data
        self.assertEquals(1,2)



