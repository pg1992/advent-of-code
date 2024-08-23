#!/usr/bin/env python
"""
"""

import fileinput


def count_escaped(string):
    count = 0
    i = 0
    s = string[1:-1]
    while i < len(s):
        if s[i] == '\\':
            i += 1
            if s[i] not in ['\\', '\"']:
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
