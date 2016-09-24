def validate_pickle_protocol(data):
    """
    :param data: a list of tuples, formatted as [('path', (ts, count)), ...]
    :return: the validated data
    raises an exception if the data isn't formatted correctly
    """
    # data should be a list
    # ts should be a unix string, not a python datetime
    # path should be a string
    # count should be an int
    # validate a random sample of tuples
    return data


def validate_plaintext_protocol(data):
    """
    :param data: newline separated text
    :return: the validated data
    raises an exception if the data isn't formatted correctly
    """
    return data