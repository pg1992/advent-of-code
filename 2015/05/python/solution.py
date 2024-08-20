#!/usr/bin/env python
"""
Solution to problem 05 of Advent of Code 2015.
"""

import fileinput


def is_nice_string(string):
    def has_three_vowels(s):
        return len([c for c in s if c in 'aeiou']) >= 3

    def has_double_letter(s):
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return True
        return False

    def has_forbidden_string(s):
        for p in ['ab', 'cd', 'pq', 'xy']:
            if p in s:
                return True
        return False

    return (has_three_vowels(string) and
           has_double_letter(string) and
           not has_forbidden_string(string))



def main():
    """Main function"""

    strings = [s.strip() for s in fileinput.input()]
    total_nice_strings = len([s for s in strings if is_nice_string(s)])
    print(f'Total nice strings: {total_nice_strings}')


if __name__ == "__main__":
    main()
