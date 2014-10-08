import datetime


def Date(format='%d-%m-%Y'):
    return lambda value: datetime.datetime.strptime(value, format)


def NotEmpty():
    return lambda value: value.strip().isspace()