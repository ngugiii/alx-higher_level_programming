#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    retur = list(a_dictionary.keys())[0]
    big = a_dictionary[retur]
    for a, b in a_dictionary.items():
        if b > big:
            big = b
            retur = a
    return (retur)
