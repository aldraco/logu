import datetime as dt

from errors import DataFormattingError

def validate_pickle_protocol(data):
    random_tuple = data[len(data) / 3]
    try:
        assert type(data) == list
        assert type(random_tuple) == tuple
        assert type(random_tuple[0]) == str
        assert type(random_tuple[1][0]) == str
        assert type(random_tuple[1][1]) == int
    except AssertionError as e:
        msg = "Data must be [(path:str, (unix_timestamp:str, count:int)), ...]"
        raise DataFormattingError(msg)
    else:
        return data