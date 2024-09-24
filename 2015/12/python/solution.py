#!/usr/bin/env python
"""
Solution for problem 12 of AoC 2015.
"""

__author__ = "Pedro Moreira"


import fileinput
import json
import pprint


def main():
    """Entrypoint."""

    json_doc = fileinput.input().readline()

    pprint.pprint(json.loads(json_doc))


if __name__ == "__main__":
    main()
