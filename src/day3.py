#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np

puzzle_input = get_puzzle_data(day=3)
example_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
bin_array = np.zeros(shape=(len(puzzle_input), len(puzzle_input[0])), dtype="bool")
bin_array_ex = np.zeros(shape=(len(example_input), len(example_input[0])), dtype="bool")
for (ii, row) in enumerate(puzzle_input):
    for (jj, c) in enumerate(row):
        bin_array[ii, jj] = c == "1"
for (ii, row) in enumerate(example_input):
    for (jj, c) in enumerate(row):
        bin_array_ex[ii, jj] = c == "1"


totals = [0 for x in puzzle_input[0]]
for x in puzzle_input:
    for (ii, c) in enumerate(x):
        if c == "0":
            totals[ii] += 1

gamma = 0
epsilon = 0
for (ii, x) in enumerate(totals):
    if x > len(puzzle_input) / 2:
        gamma += 2 ** (len(totals) - ii - 1)
    else:
        epsilon += 2 ** (len(totals) - ii - 1)

gamma * epsilon


def convert_to_int(bool_array):
    positive = 0
    complement = 0
    for (ii, x) in enumerate(bool_array):
        if x:
            positive += 2 ** (np.shape(bool_array)[0] - ii - 1)
        else:
            complement += 2 ** (np.shape(bool_array)[0] - ii - 1)
    return positive, complement


def get_most_common(bool_array, digit):
    one_is_most_common = np.sum(bool_array, axis=0) >= bool_array.shape[0] / 2
    rows_with_most_common = one_is_most_common[digit] == bool_array[:, digit]
    only_most_common = bool_array[rows_with_most_common, :]
    return only_most_common


def get_least_common(bool_array, digit):
    one_is_least_common = np.sum(bool_array, axis=0) < bool_array.shape[0] / 2
    rows_with_least_common = one_is_least_common[digit] == bool_array[:, digit]
    only_least_common = bool_array[rows_with_least_common, :]
    return only_least_common


def filter_via(bool_array, f):
    filtered = np.copy(bool_array)
    n_dims = bool_array.shape[1]
    for digit in range(n_dims):
        filtered = f(filtered, digit)
        if np.shape(filtered)[0] == 1:
            break
    return filtered[0, :]


# debug example
print(convert_to_int(filter_via(bin_array_ex, get_most_common)))
print(convert_to_int(filter_via(bin_array_ex, get_least_common)))

# actual data
oxygen = convert_to_int(filter_via(bin_array, get_most_common))[0]
C02 = convert_to_int(filter_via(bin_array, get_least_common))[0]
print(oxygen)
print(C02)
print(oxygen * C02)


if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    bin_array = np.zeros(shape=(len(puzzle_input), len(puzzle_input[0])), dtype="bool")
    print(f"{count_increase(sea_depths)}")
