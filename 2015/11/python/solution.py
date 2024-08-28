#!/usr/bin/env python
"""
Solution to problem 11 of AoC 2015.
"""
__author__ = "Pedro Moreira"


import fileinput


def string_to_num_list(string):
    """Return a list os numbers from 0 to 25, where 'a' is considered 0 and z
    is 25.

    >>> string_to_num_list("abc")
    [0, 1, 2]
    >>> string_to_num_list("zcde")
    [25, 2, 3, 4]
    >>> string_to_num_list("aaaaa")
    [0, 0, 0, 0, 0]
    """

    return [ord(c) - ord('a') for c in string]


def num_list_to_string(numl):
    """Convert a sequence of numbers to string.

    >>> num_list_to_string([0, 0, 0])
    'aaa'
    >>> num_list_to_string([25, 24, 23])
    'zyx'
    >>> num_list_to_string([10, 10, 10, 10])
    'kkkk'
    """

    return ''.join([chr(ord('a') + c) for c in numl])


def add_strings(sa, sb):
    """Add two strings as if they are numbers, with 'a' being 0, and so on.

    >>> add_strings("aaa", "aaa")
    'aaa'
    >>> add_strings("aaa", "aab")
    'aab'
    >>> add_strings("aaa", "b")
    'aab'
    >>> add_strings("aaa", "ba")
    'aba'
    >>> add_strings("aaz", "b")
    'aba'
    >>> add_strings("za", "ba")
    'baa'
    """

    if len(sa) > len(sb):
        sb = 'a' * (len(sa) - len(sb)) + sb
    elif len(sb) > len(sa):
        sa = 'a' * (len(sb) - len(sa)) + sa

    san = string_to_num_list(sa)
    sbn = string_to_num_list(sb)

    res = []
    carry = 0
    for i in range(len(sa)):
        k = len(sa) - i - 1
        s = san[k] + sbn[k] + carry
        res.append(s % 26)
        carry = s // 26
    else:
        if carry > 0:
            res.append(carry)

    return num_list_to_string(res[::-1])


def satisfies_req_1(s):
    """Has 3 chars in sequence.

    >>> satisfies_req_1('hijklmmn')
    True
    >>> satisfies_req_1('abbcdffg')
    True
    >>> satisfies_req_1('abbedffg')
    False
    """

    for a, b, c in zip(s, s[1:], s[2:]):
        if ord(b) - ord(a) == 1 and ord(c) - ord(b) == 1:
            return True

    return False


def satisfies_req_2(s):
    """String does not contain 'i', 'l', or 'o'.

    >>> satisfies_req_2('aabb')
    True
    >>> satisfies_req_2('aaibb')
    False
    >>> satisfies_req_2('aajbo')
    False
    >>> satisfies_req_2('abcd')
    True
    """

    return all(c not in 'iol' for c in s)


def satisfies_req_3(s):
    """String conatains 2 or more non-overlapping pairs of equal chars.

    >>> satisfies_req_3('aaa')
    False
    >>> satisfies_req_3('aaaa')
    True
    >>> satisfies_req_3('aabbaa')
    True
    """

    i = 0
    count = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            i += 1
            count += 1
        i += 1

    return count > 1


def is_valid_password(string):
    """

    >>> is_valid_password("hijklmmn")
    False
    >>> is_valid_password("abcdefgh")
    False
    >>> is_valid_password("abcdffaa")
    True
    >>> is_valid_password("ghijklmn")
    False
    >>> is_valid_password("ghjaabcc")
    True
    """

    return all(
        req(string) for req in [
            satisfies_req_1,
            satisfies_req_2,
            satisfies_req_3,
        ]
    )


def main():
    """Entrypoint

    Get input and call each solution step.
    """

    current_password = fileinput.input().readline()

    while not is_valid_password(current_password):
        current_password = add_strings(current_password, 'b')

    print('Next correct password:', current_password)

    current_password = add_strings(current_password, 'b')

    while not is_valid_password(current_password):
        current_password = add_strings(current_password, 'b')

    print('Next correct password:', current_password)


if __name__ == "__main__":
    main()
