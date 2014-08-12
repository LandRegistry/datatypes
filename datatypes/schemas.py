from voluptuous import Schema, Required, Optional, All, Length


address_schema = Schema({
    Required('line_one'): {str: All(Length(max=40))},
    Optional('line_two'): {str: All(Length(max=40))},
    Optional('line_three'): {str: All(Length(max=40))},
    Optional('line_four'): {str: All(Length(max=40))},
    Required('city'): {str: All(Length(max=40))},
    Required('postcode'): str
})