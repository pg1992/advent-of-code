#!/usr/bin/env python

def final_floor(instructions):
    floor = 0
    for instruction in instructions:
        if instruction == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def basement_position(instructions):
    floor = 0
    i = 0
    while i < len(instructions) and floor > -1:
        if instructions[i] == '(':
            floor += 1
        else:
            floor -= 1
        i += 1
    return i


def main():
    instructions = input()

    print(f'Final floor: {final_floor(instructions)}')
    print(f'Basement position: {basement_position(instructions)}')


if __name__ == "__main__":
    main()
