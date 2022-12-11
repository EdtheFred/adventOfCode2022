# Imports
import numpy as np
import re

# Part functions
def part_1():

    # Path for data
    path = 'day_5/day_5_input.txt'
    
    # Read in data
    with open(path) as f:
        lines = f.read().splitlines()

    # Create matrices
    stacks = {}
    instructions = []
    stackCheck = True
    for line in lines:
        if stackCheck:
            stack = 1
            for idx in range(1,len(line),4):
                if line[idx].isalpha():
                    if not stack in stacks:
                        stacks[stack] = [line[idx]]
                    else:
                        stacks[stack].append(line[idx])
                stack += 1
        else:
            instructions.append([int(i) for i in re.findall(r'\d+', line)])
        if not line:
            stackCheck = False
    
    for stack in stacks:
        stacks[stack].reverse()

    # Solution
    # Instructions [moves, from, to]
    for instr in instructions:
        moves = instr[0]
        mfrom = instr[1]
        mto = instr[2]

        for mov in range(moves):
            curr_char = stacks[mfrom][-1]
            stacks[mfrom].pop(-1)
            stacks[mto].append(curr_char)

    # Get solution
    sol = ''
    for key in dict(sorted(stacks.items())):
        sol += stacks[key][-1]

    sol_1 = sol
    print('Part 1: {}'.format(sol_1))

def part_2():

    # Path for data
    path = 'day_5/day_5_input.txt'
    
    # Read in data
    with open(path) as f:
        lines = f.read().splitlines()

    # Create matrices
    stacks = {}
    instructions = []
    stackCheck = True
    for line in lines:
        if stackCheck:
            stack = 1
            for idx in range(1,len(line),4):
                if line[idx].isalpha():
                    if not stack in stacks:
                        stacks[stack] = [line[idx]]
                    else:
                        stacks[stack].append(line[idx])
                stack += 1
        else:
            instructions.append([int(i) for i in re.findall(r'\d+', line)])
        if not line:
            stackCheck = False
    
    for stack in stacks:
        stacks[stack].reverse()

    # Solution
    # Instructions [moves, from, to]
    for instr in instructions:
        moves = instr[0]
        mfrom = instr[1]
        mto = instr[2]

        curr_move = stacks[mfrom][-moves:]
        for i in range(moves):
            stacks[mfrom].pop(-1)

        for c in curr_move:
            stacks[mto].append(c)

    # Get solution
    sol = ''
    for key in dict(sorted(stacks.items())):
        sol += stacks[key][-1]

    sol_2 = sol
    print('Part 2: {}'.format(sol_2))

# Main
def main():
    # Part 1
    part_1()

    # Part 2
    part_2()

if __name__ == "__main__":
    main()

