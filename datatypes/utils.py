def filter_none(dictionary):
    return {k: v for k, v in dictionary.iteritems() if v is not None}


def translate_voluptous_errors(voluptuous_exception):
    return {e.path[0]: translate_error(e.error_message)
            for e in voluptuous_exception.errors
            if e.path is not [] and e.path is not None}


def translate_error(message):
    # TODO: Translate voluptuous errors into generic useful form
    return message