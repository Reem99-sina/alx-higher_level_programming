#!/usr/bin/python3
def add_integer(a, b=98):
    """
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
