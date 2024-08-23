#!/usr/bin/env python
"""
Solution for problem 9 of AoC 2015.
"""

__author__ = "Pedro Moreira"

import fileinput
from itertools import permutations


def perms(l):
    """Return all the permutations of the elements of `l`.

    .. note:: I didn't know about `itertools.permutations` when I wrote this :P
    and I also did not know about that wizard shit:
    https://stackoverflow.com/a/64341432/4088670
    """

    if len(l) == 1:
        return [l]

    a = l[0]
    ls = perms(l[1:])

    lss = []
    for p in ls:
        for i in range(len(p) + 1):
            t = p[:i] + [a] + p[i:]
            lss.append(t)

    return lss


def dist(l, graph):
    """Find the distance of path `l` given distances in `graph`."""

    d = 0
    for i in range(len(l) - 1):
        d += graph[(l[i], l[i+1])]

    return d


def main():
    """main"""

    paths = [d.strip() for d in fileinput.input()]
    graph = {}
    places = []
    for p in paths:
        a, _, b, _, d = p.split(' ')
        if a not in places:
            places.append(a)
        if b not in places:
            places.append(b)
        graph[(a, b)] = graph[(b, a)] = int(d)

    ds = [dist(p, graph) for p in permutations(places)]
    print('min dist =', min(ds))
    print('max dist =', max(ds))


if __name__ == "__main__":
    main()
