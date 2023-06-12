#!/usr/bin/python3
def lookup(obj):
    """
    Given an object, returns a list of its available attributes and methods.
    """
    attrs=[]
    for attr in dir(obj):
        if  attr.startswith('__'):
           attrs.append(attr);
    return attrs;
