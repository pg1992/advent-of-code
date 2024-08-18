#!/usr/bin/env python

import fileinput


def total_area(dims):
    s = 0
    for a, b, c in dims:
        s += 2*(a*b + a*c + b*c) + a*b
    return s


def main():
    dims = [sorted(map(int, line.strip().split('x'))) for line in fileinput.input()]
    print(f'Total area needed = {total_area(dims)}')


if __name__ == "__main__":
    main()
