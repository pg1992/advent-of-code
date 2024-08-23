#!/usr/bin/env python
"""
Solution of problem 8 of AoC 2015.
"""

import fileinput


def count_escaped(string):
    """Count `len` of `string` after escaping and removing surrounding `"`"""

    count = 0
    i = 0
    s = string[1:-1]

    while i < len(s):
        if s[i] == '\\':
            i += 1
            if s[i] == 'x':
                i += 2
        count += 1
        i += 1

    return count


def main():
    """Entrypoint"""

    words = [s.strip() for s in fileinput.input()]

    total = sum([len(w) - count_escaped(w) for w in words])
    print('Total =', total)


if __name__ == "__main__":
    main()
