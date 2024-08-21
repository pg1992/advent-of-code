#!/usr/bin/env python

"""
Solution for problem 7 of AoC 2015.
"""

import fileinput


def compute(wire, sig):
    """Compute using dynamic programming and recursion."""

    op = wire[sig]

    if isinstance(op, int):
        return op

    if len(op) == 1:
        if op[0].isnumeric():
            val = int(op[0])
        else:
            val = compute(wire, op[0])
    elif len(op) == 2:
        assert op[0] == 'NOT'
        val = 0xffff ^ compute(wire, op[1])
    else:
        assert len(op) == 3
        x = int(op[0]) if op[0].isnumeric() else compute(wire, op[0])
        if op[1] == 'LSHIFT':
            val = x << int(op[2])
        elif op[1] == 'RSHIFT':
            val =  x >> int(op[2])
        else:
            y = int(op[2]) if op[2].isnumeric() else compute(wire, op[2])
            if op[1] == 'AND':
                val = x & y
            else:
                assert op[1] == 'OR'
                val = x | y

    wire[sig] = val
    return val


def circuit(booklet):
    """Create a hashmap of the connections"""

    wire = {}

    for ins in booklet:
        t = ins.split(' ')
        wire[t[-1]] = t[:-2]

    return wire


def main():
    """Entry point."""

    booklet = [s.strip() for s in fileinput.input()]

    wire = circuit(booklet)
    sig_a = compute(wire, 'a')
    print(sig_a)

    wire = circuit(booklet)
    wire['b'] = sig_a
    print(compute(wire, 'a'))


if __name__ == "__main__":
    main()
