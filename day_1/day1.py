# Imports
import numpy as np

# Part functions
def part_1():

    # Create data matrix
    path = 'day_1/day_1_input.txt'
    with open(path) as f:
        lines = f.read().splitlines()
    
    elve_iter = 1
    data = {}
    curr_elve = []
    for line in lines:
        curr_key = 'Elve {}'.format(elve_iter)
        if line:
            curr_elve.append(int(line))
        else:
            data[curr_key] = curr_elve
            curr_elve = []
            elve_iter += 1

    max = -1
    max_idx = -1
    for key in data:
        curr_max = np.sum(data[key])
        curr_idx = key

        if curr_max > max:
            max = curr_max
            max_idx = curr_idx

    sol_1 = max
    print(max_idx)
    print('Part 1: {}'.format(sol_1))

def part_2():

    # Create data matrix
    path = 'day_1/day_1_input.txt'
    with open(path) as f:
        lines = f.read().splitlines()
    
    elve_iter = 1
    data = {}
    curr_elve = []
    for line in lines:
        curr_key = 'Elve {}'.format(elve_iter)
        if line:
            curr_elve.append(int(line))
        else:
            data[curr_key] = curr_elve
            curr_elve = []
            elve_iter += 1

    sorted_list = []
    sorted_list = sorted(data, key=data.get, reverse=True)
    print(sorted_list)

    sol_2 = 'nan'
    print('Part 2: {}'.format(sol_2))

# Main
def main():
    # Part 1
    part_1()

    # Part 2
    part_2()


if __name__ == "__main__":
    main()

