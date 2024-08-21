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


def is_even_nicer_string(string):
    def has_pair_twice(s):
        for i in range(len(s)-2):
            pair = s[i:i+2]
            subs = s[:i] + '**' + s[i+2:]
            if pair in subs:
                return True
        return False

    def has_repeated_letter(s):
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                return True
        return False

    return has_pair_twice(string) and has_repeated_letter(string)



def main():
    """Main function"""

    strings = [s.strip() for s in fileinput.input()]

    total_nice_strings = len([s for s in strings if is_nice_string(s)])
    print(f'Total nice strings: {total_nice_strings}')

    total_nicer_strings = len([s for s in strings if is_even_nicer_string(s)])
    print(f'Total nicer strings: {total_nicer_strings}')


if __name__ == "__main__":
    main()
