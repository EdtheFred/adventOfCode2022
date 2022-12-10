# Imports
import numpy as np

# Get priority of item
def get_priority(letter):
    if letter.islower():
        # 97-122 -> 1-26
        return ord(letter)-96
    else:
        # 65-90 -> 27-52
        return ord(letter)-38


# Part functions
def part_1():

    # Create data matrix
    path = 'day_3/day_3_input.txt'
    
    with open(path) as f:
        lines = f.read().splitlines()
    
    sum = 0
    for line in lines:
        first = [line[i:i+int(len(line)/2)] for i in range(0, len(line), int(len(line)/2))][0]
        second = [line[i:i+int(len(line)/2)] for i in range(0, len(line), int(len(line)/2))][1]
        
        used = []
        for i in first: 
            if i in second:
                if not i in used:
                    sum = sum + get_priority(i)
                    used.append(i)

    sol_1 = sum
    print('Part 1: {}'.format(sol_1))

def part_2():

    # Create data matrix
    path = 'day_3/day_3_input.txt'
    
    with open(path) as f:
        lines = f.read().splitlines()
    
    sum = 0
    for idx in range(0,len(lines),3):
        first = lines[idx]
        second = lines[idx+1]
        third = lines[idx+2]
        
        used = []
        for i in first: 
            for j in second:
                for k in third:
                    if i == j == k:
                        if not i in used:
                            sum = sum + get_priority(i)
                            used.append(i)

    sol_2 = sum
    print('Part 2: {}'.format(sol_2))

# Main
def main():
    # Part 1
    part_1()

    # Part 2
    part_2()

if __name__ == "__main__":
    main()

