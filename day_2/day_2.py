# Imports
import numpy as np

# Part functions
def part_1():

    # Create data matrix
    path = 'day_2/day_2_input.txt'
    
    with open(path) as f:
        lines = f.read().splitlines()
    
    data = []
    for line in lines:
        temp = [line[0], line[2]]
        data.append(temp)

    score = 0
    for row in data:
        opp = row[0]
        me = row[1]
        if opp == 'A':
            opp = 'X'
        elif opp == 'B':
            opp = 'Y'
        elif opp == 'C':
            opp = 'Z'

        if me == 'X':
            score = score + 1
        elif me == 'Y':
            score = score + 2
        elif me == 'Z':
            score = score + 3

        if opp == me:
            score = score + 3
        elif opp == 'X' and me == 'Y':
            score = score + 6
        elif opp == 'Y' and me == 'Z':
            score = score + 6
        elif opp == 'Z' and me == 'X':
            score = score + 6

    sol_1 = score
    print('Part 1: {}'.format(sol_1))

def part_2():

    # Create data matrix
    path = 'day_2/day_2_input.txt'
    
    with open(path) as f:
        lines = f.read().splitlines()
    
    data = []
    for line in lines:
        temp = [line[0], line[2]]
        data.append(temp)

    score = 0

    for row in data:
        opp = row[0]
        me = row[1]

        if me == 'X': # loss
            if opp == 'A':
                score = score + 3
            elif opp == 'B':
                score = score + 1
            elif opp == 'C':
                score = score + 2
        elif me == 'Y': # draw
            score = score + 3
            if opp == 'A':
                score = score + 1
            elif opp == 'B':
                score = score + 2
            elif opp == 'C':
                score = score + 3
        elif me == 'Z': # win
            score = score + 6
            if opp == 'A':
                score = score + 2
            elif opp == 'B':
                score = score + 3
            elif opp == 'C':
                score = score + 1

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

