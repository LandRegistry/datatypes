import unittest

from datatypes.validators import postcode_validator


class TestPostcodeValidation(unittest.TestCase):
    def setUp(self):
        self.postcode_validator = postcode_validator()

