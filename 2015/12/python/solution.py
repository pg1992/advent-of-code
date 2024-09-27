#!/usr/bin/env python
"""
Solution for problem 12 of AoC 2015.
"""

__author__ = "Pedro Moreira"


import fileinput
import json
import pprint


def find_sum(json_doc):
    """
    >>> find_sum(2)
    2
    >>> find_sum([1, 2])
    3
    >>> find_sum([[1, 2]])
    3
    >>> find_sum([1,2,3])
    6
    >>> find_sum({"a":2,"b":4})
    6
    >>> find_sum([[[3]]])
    3
    >>> find_sum({"a":{"b":4},"c":-1})
    3
    >>> find_sum({"a":[-1,1]})
    0
    >>> find_sum([-1,{"a":1}])
    0
    >>> find_sum([])
    0
    >>> find_sum({})
    0
    """

    if isinstance(json_doc, int):
        return json_doc
    elif isinstance(json_doc, list):
        if json_doc:
            return sum(find_sum(x) for x in json_doc)
        else:
            return 0
    elif isinstance(json_doc, dict):
        if json_doc:
            return sum(find_sum(x) for x in json_doc.values())
        else:
            return 0
    return 0


def main():
    """Entrypoint."""

    json_doc = json.loads(fileinput.input().readline())

    print(find_sum(json_doc))


if __name__ == "__main__":
    main()
