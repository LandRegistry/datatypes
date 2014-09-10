import unittest

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes import title_validator

class TestTitleValidation(unittest.TestCase):
    def test_can_validate_title(self):
        try:
            title_validator.validate({})
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate title: " + repr(e))
