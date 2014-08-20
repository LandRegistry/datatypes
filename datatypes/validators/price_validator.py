# -*- coding: utf-8 -*-

from voluptuous import All, Match
from datatypes.core import SingleValueValidator

price_schema = All(Match('^(£?)?[0-9]+(,[0-9]+)?(\.\d{1,2})?$'))


class Price(SingleValueValidator):
    def __init__(self):
        super(Price, self).__init__()

    def define_schema(self):
        return price_schema

    def define_error_message(self):
        return "Price must be a numeric value in pounds"
