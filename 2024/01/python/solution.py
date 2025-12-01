#!/usr/bin/env python

import fileinput


def main():
    ll: list[int] = []
    rl: list[int] = []
    for line in fileinput.input():
        x, y = line.split()
        ll.append(int(x))
        rl.append(int(y))

    s = 0
    for x, y in zip(sorted(ll), sorted(rl)):
        s += abs(x - y)

    print(s)

    sc = 0
    for n in ll:
        sc += n * rl.count(n)

    print(sc)


if __name__ == "__main__":
    main()
