#!/usr/bin/env python

import fileinput
import re


def main():
    p = re.compile(r'mul\(\d+,\d+\)')
    s = 0
    for line in fileinput.input():
        nums = [op[4:-1].split(',') for op in p.findall(line)]
        s += sum(int(x) * int(y) for x, y in nums)
    print(s)


if __name__ == "__main__":
    main()
