#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin
from string import digits


def find_num(line: str) -> int:
    ds = [d for d in line if d in digits]
    num = int(ds[0]) * 10 + int(ds[-1])

    return num


def retarded_to_sensible(line: str) -> str:
    WORD_LIST = [
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
        ('5', 'five'),
        ('6', 'six'),
        ('7', 'seven'),
        ('8', 'eight'),
        ('9', 'nine'),
    ]

    word = ""
    processed = ""
    for c in line:
        if c in digits:
            word = ""
            processed += c
        else:
            word += c
            for n, s in WORD_LIST:
                ...


    return processed


def find_retarded_num(retarded: str) -> int:
    sensible = retarded_to_sensible(retarded)
    print(f"retarded = {retarded}")
    print(f"sensible = {sensible}")
    return find_num(sensible)


if __name__ == "__main__":
    s = 0
    s_retarded = 0
    for line in stdin:
        line = line.strip()
        s += find_num(line)
        s_retarded += find_retarded_num(line)

    print(f"s = {s}")
    print(f"s_retarded = {s_retarded}")
