#!/usr/bin/env python

import fileinput
from hashlib import md5


def find_hash(key, leading_zeroes=5):
    mask = '0' * leading_zeroes
    i = 0

    while True:
        curr_hash = md5(key + str(i).encode('utf-8')).hexdigest()
        if curr_hash[:leading_zeroes] == mask:
            break
        i += 1

    return i


def main():
    key = fileinput.input(encoding='utf-8').readline()
    print(find_hash(key.encode('utf-8')))
    print(find_hash(key.encode('utf-8'), 6))


if __name__ == "__main__":
    main()
