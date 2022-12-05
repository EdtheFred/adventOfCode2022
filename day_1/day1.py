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

    data_mean = {}
    for key, value in data.items():
        data_mean[key] = np.sum(value)

    data_sorted = dict(sorted(data_mean.items(), key=lambda item: item[1]))
    data_keys = list(data_sorted.keys())
    data_val = list(data_sorted.values())

    sum = 0
    for i in range(1,4,1):
        sum = sum + float(data_val[-i])

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

