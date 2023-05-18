#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    exclusive_set_1 = set_1 - set_2
    
    # Compute the set of elements that are exclusive to set_2
    exclusive_set_2 = set_2 - set_1
    
    # Compute the set of all exclusive elements
    exclusive_set = exclusive_set_1 | exclusive_set_2
    
    return exclusive_set
