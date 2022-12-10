# Imports
import numpy as np
import re

# Part functions
def part_1():

    # Create data matrix
    path = 'day_4/day_4_input.txt'
    
    with open(path) as f:
        lines = f.read().splitlines()

    score = 0
    for line in lines:
        numbers = [int(i) for i in re.findall(r'\d+', line)]
        elve_1 = [i for i in range(numbers[0],numbers[1]+1,1)]
        elve_2 = [i for i in range(numbers[2],numbers[3]+1,1)]

        check_1 = all(item in elve_1 for item in elve_2)
        check_2 = all(item in elve_2 for item in elve_1)

        if check_1 or check_2:
            score += 1


    sol_1 = score
    print('Part 1: {}'.format(sol_1))

def part_2():

    # Create data matrix
    path = 'day_4/day_4_input.txt'
    
    with open(path) as f:
        lines = f.read().splitlines()

    score = 0
    for line in lines:
        numbers = [int(i) for i in re.findall(r'\d+', line)]
        elve_1 = [i for i in range(numbers[0],numbers[1]+1,1)]
        elve_2 = [i for i in range(numbers[2],numbers[3]+1,1)]

        check_1 = any(item in elve_1 for item in elve_2)
        check_2 = any(item in elve_2 for item in elve_1)

        if check_1 or check_2:
            score += 1
    
    sol_2 = score
    print('Part 2: {}'.format(sol_2))

# Main
def main():
    # Part 1
    part_1()

    # Part 2
    part_2()

if __name__ == "__main__":
    main()

