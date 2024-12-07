#!/usr/bin/env python

import fileinput
import re


def main():
    process = True
    p = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    s = 0
    for line in fileinput.input():
        for token in p.findall(line):
            if token == "do()":
                process = True
            elif token == "don't()":
                process = False
            elif process:
                nums = [int(n) for n in token[4:-1].split(',')]
                s += nums[0] * nums[1]
    print(s)


if __name__ == "__main__":
    main()
