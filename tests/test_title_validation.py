# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

from datatypes.exceptions import DataDoesNotMatchSchemaException

from datatypes import title_validator

simple_title = {
    'title_number': 'TEST123456789',
    'payment': {
        'price_paid': '3100.00'
    }
}

class TestTitleValidation(unittest.TestCase):
    def test_can_validate_valid_title(self):
        try:
            title_validator.validate(simple_title)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Could not validate title: " + repr(e))

    def test_cannot_validate_invalid_title_number(self):
        bad_title = deepcopy(simple_title)
        del bad_title['title_number']
        self.assertRaisesRegexp(DataDoesNotMatchSchemaException, 'title_number is a required field', title_validator.validate, bad_title)

    def test_cannot_validate_invalid_title_price_paid(self):
        bad_title = deepcopy(simple_title)
        bad_title['payment']['price_paid'] = '£3100.00'
        self.assertRaises(DataDoesNotMatchSchemaException, title_validator.validate, bad_title)
