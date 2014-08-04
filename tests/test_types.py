import unittest

import sys


class TestTypes(unittest.TestCase):
    def __init__(self):
        print "creating path"

        for d in sys.path:
            print d

