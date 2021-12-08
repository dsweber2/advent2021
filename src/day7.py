#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np
import statistics

puzzle_input = get_puzzle_data(day=7)
example_input = ["16,1,2,0,4,2,7,1,2,14"]


def process_input(inn):
    return list(map(int, inn[0].split(",")))


full_list = np.array(process_input(puzzle_input))
print(np.linalg.norm(full_list,))
print(statistics.median(full_list))
print(np.linalg.norm(np.array(full_list) - statistics.median(full_list), ord=1))

print(np.round(statistics.mean(full_list)))
print(
    np.linalg.norm(np.array(full_list) - np.round(statistics.mean(full_list)), ord=2)
    ** 2
)
distances = abs(np.array(full_list) - np.round(statistics.mean(full_list)))
distances
max(full_list)
loc = 5


def calc_cost(full_list, loc):
    distances = abs(full_list - loc)
    costs = (distances + 1) * distances
    return np.sum(costs) / 2


max_val = np.Inf
max_loc = 0
for loc in range(max(full_list)):
    loc_val = calc_cost(full_list, loc)
    if loc_val < max_val:
        print(f"{loc_val}, {loc}")
        max_val = loc_val
        max_loc = loc


if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    bin_array = np.zeros(shape=(len(puzzle_input), len(puzzle_input[0])), dtype="bool")
    print(f"{count_increase(sea_depths)}")
