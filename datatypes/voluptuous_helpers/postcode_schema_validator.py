from functools import wraps
import re
from voluptuous import Invalid

inward = 'ABDEFGHJLNPQRSTUWXYZ'
fst = 'ABCDEFGHIJKLMNOPRSTUWYZ'
sec = 'ABCDEFGHKLMNOPQRSTUVWXY'
thd = 'ABCDEFGHJKSTUW'
fth = 'ABEHMNPRVWXY'


def postcode_is_valid():
    @wraps(postcode_is_valid)
    def f(postcode):
        if not (re.match('[%s][1-9]\d[%s][%s]$' % (fst, inward, inward), postcode) or
                    re.match('[%s][1-9]\d\d[%s][%s]$' % (fst, inward, inward), postcode) or
                    re.match('[%s][%s]\d\d[%s][%s]$' % (fst, sec, inward, inward), postcode) or
                    re.match('[%s][%s][1-9]\d\d[%s][%s]$' % (fst, sec, inward, inward), postcode) or
                    re.match('[%s][1-9][%s]\d[%s][%s]$' % (fst, thd, inward, inward), postcode) or
                    re.match('[%s][%s][1-9][%s]\d[%s][%s]$' % (fst, sec, fth, inward, inward), postcode)):
            raise Invalid("Postcode is invalid: " + postcode)
        return postcode

    return f

