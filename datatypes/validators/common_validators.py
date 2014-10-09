import dateutil.parser


def Date():
    return lambda value: dateutil.parser.parse(value)

def NotEmpty():
    return lambda value: value.strip().isspace()