import unittest

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes.validators.postcode_validator import Postcode


class TestPostcodeValidation(unittest.TestCase):
    def setUp(self):
        self.postcode_validator = Postcode()

    def test_can_validate_postcode(self):
        try:
            self.postcode_validator.validate("WC2B6SE")
            self.postcode_validator.validate("wc2b6se")
            self.postcode_validator.validate("wc2b 6se")
            self.postcode_validator.validate("Wc2b  6se")
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate postcode: " + repr(e))

    def test_does_not_validate_invalid_postcode(self):
        self.assertRaises(DataDoesNotMatchSchemaException, self.postcode_validator.validate, "sausages")

    def test_can_convert_postcode_to_canonical_form(self):
        self.assertEqual(self.postcode_validator.to_canonical_form("wc2B6sE"), "WC2B 6SE")


