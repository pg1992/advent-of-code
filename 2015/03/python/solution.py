#!/usr/bin/env python

import fileinput


def next_position(d, x, y):
    dx, dy = 0, 0

    if d == '^':
        dy = 1
    elif d == 'v':
        dy = -1
    elif d == '>':
        dx = 1
    elif d == '<':
        dx = -1

    return x + dx, y + dy


def count_houses(dirs):
    houses = {}
    cur_pos = (0, 0)
    houses[cur_pos] = 1
    for d in dirs:
        cur_pos = next_position(d, *cur_pos)
        houses[cur_pos] = houses.get(cur_pos, 0) + 1
    return len(houses)


def main():
    dirs = fileinput.input().readline()
    print(f'Visited houses = {count_houses(dirs)}')


if __name__ == "__main__":
    main()
