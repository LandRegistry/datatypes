def filter_none_from_dictionary(dictionary):
    filtered = {}

    for k, v in dictionary.iteritems():
        if isinstance(v, dict):
            filtered[k] = filter_none_from_dictionary(v)
        else:
            if v is not None:
                filtered[k] = v

    return filtered


def alphabetically_sorted_dict(d):
    """
    Returns a dictionary with all keys recursively sorted alphabetically
    """
    ordered = OrderedDict()
    for k, v in sorted(d.items()):
        if isinstance(v, dict):
            ordered[k] = alphabetically_sorted_dict(v)
        else:
            ordered[k] = v
    return ordered


def translate_voluptous_errors(voluptuous_exception):
    return {e.path[0]: translate_error(e.error_message)
            for e in voluptuous_exception.errors
            if e.path is not [] and e.path is not None}


def translate_error(message):
    # TODO: Translate voluptuous errors into generic useful form
    return message