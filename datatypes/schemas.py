from voluptuous import Required, Optional, All, Length

postcode_schema = All(str)

address_schema = {
    Required('line_one'): All(str, Length(max=40)),
    Optional('line_two'): All(str, Length(max=40)),
    Optional('line_three'): All(str, Length(max=40)),
    Optional('line_four'): All(str, Length(max=40)),
    Required('city'): All(str, Length(max=40)),
    Required('postcode'): postcode_schema
}


