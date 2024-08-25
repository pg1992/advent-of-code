#!/usr/bin/env python
"""
"""

__author__ = "Pedro Moreira"


import fileinput


def look_and_say(num):
    """"""

    s = 1
    res = ''
    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            s += 1
        else:
            res += f'{s}{num[i-1]}'
            s = 1
    res += f'{s}{num[-1]}'

    return res


def main():
    """Entrypoint"""

    number = fileinput.input().readline()

    assert '11' == look_and_say('1')
    assert '21' == look_and_say('11')
    assert '1211' == look_and_say('21')
    assert '312211' == look_and_say('111221')

    for _ in range(40):
        number = look_and_say(number)

    print('The length of the result is', len(number))

    for _ in range(10):
        number = look_and_say(number)

    print('The length of the result is', len(number))


if __name__ == "__main__":
    main()
