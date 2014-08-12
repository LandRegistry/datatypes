from voluptuous import Schema, Required, Optional, All, Length


address_schema = Schema({
    Required('line_one'): All(str, Length(max=40)),
    Optional('line_two'): All(str, Length(max=40)),
    Optional('line_three'): All(str, Length(max=40)),
    Optional('line_four'): All(str, Length(max=40)),
    Required('city'): All(str, Length(max=40)),
    Required('postcode'): All(str)
})