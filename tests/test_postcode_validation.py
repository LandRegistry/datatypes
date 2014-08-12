import unittest

from datatypes.validators import PostcodeValidator


class TestPostcodeValidation(unittest.TestCase):
    def setUp(self):
        self.postcode_validator = PostcodeValidator()

