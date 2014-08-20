import unittest

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes.validators.postcode_validator import Postcode


class TestPostcodeValidation(unittest.TestCase):
    def setUp(self):
        self.postcode_validator = Postcode()

    def test_can_validate_postcode(self):
        try:
            self.postcode_validator.validate("WC2B6SE")
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate postcode: " + repr(e))


