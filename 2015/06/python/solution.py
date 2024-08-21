#!/usr/bin/env python
"""
Solution for day 6 of Advent of Code 2015.
"""

import fileinput


def christimas_lights(inss):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for ins in inss:
        t = ins.split(' ')
        pi, pf = 0, 0
        op = lambda x: x

        if t[0] == 'turn':
            pi, pf = 2, 4
            if t[1] == 'on':
                op = lambda x: 1
            else:
                op = lambda x: 0
        else:
            pi, pf = 1, 3
            op = lambda x: 1 - x

        xi, yi = map(int, t[pi].split(','))
        xf, yf = map(int, t[pf].split(','))
        for x in range(xi, xf + 1):
            for y in range(yi, yf + 1):
                lights[x][y] = op(lights[x][y])

    return sum([sum(l) for l in lights])


def main():
    """Main function"""

    instructions = [line.strip() for line in fileinput.input()]
    total_lit_lights = christimas_lights(instructions)

    print('How many lights are lit?', total_lit_lights)


if __name__ == "__main__":
    main()
