#!/usr/bin/env python3

from shared import get_puzzle_data
import numpy as np
import statistics
from itertools import permutations
from itertools import count
from functools import reduce
from copy import copy
from copy import deepcopy


puzzle_input = get_puzzle_data(day=11)
example_input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]


def parse_input(inn):
    return np.array([[int(string) for string in line] for line in inn])


def step1(inn):
    return inn + 1


def check_in_bounds(ind, shape):
    if (ind[0] < 0) | (ind[0] >= shape[0]):
        return False
    if (ind[1] < 0) | (ind[1] >= shape[1]):
        return False
    return True


def all_adjacent(ind):
    y, x = ind
    return [
        [y + 1, x],
        [y, x + 1],
        [y + 1, x + 1],
        [y - 1, x],
        [y - 1, x + 1],
        [y - 1, x - 1],
        [y, x - 1],
        [y + 1, x - 1],
    ]


def get_neighbors(indices, shape):
    neighbors = []
    for ind in indices:
        neighbors.extend(all_adjacent(ind))
    neighbors_in_bounds = np.array([x for x in neighbors if check_in_bounds(x, shape)])
    return neighbors_in_bounds


def update_neighbors(indices, target_matrix):
    for ind in indices:
        target_matrix[ind[0], ind[1]] += 1


def step2(inn):
    out_mat = deepcopy(inn)
    flashing = inn > 9
    if not np.any(flashing):
        return out_mat, 0
    flashed = np.zeros(shape=inn.shape, dtype=bool)
    for _ in range(inn.size):
        # if all that are going to flash have already done so, we're done
        if (flashed == flashing).all():
            break
        # only update those not already flashed
        not_yet_flashed = flashing & (np.bitwise_not(flashed))
        not_flashed_inds = np.transpose(np.nonzero(not_yet_flashed))
        shape = inn.shape
        neighbors_in_bounds = get_neighbors(not_flashed_inds, inn.shape)
        update_neighbors(neighbors_in_bounds, out_mat)
        flashed = flashed | flashing  # record the entries which flashed
        flashing = out_mat > 9  # find new locations to flash
    n_flashes = np.sum(flashing)
    return out_mat, n_flashes


def step3(inn):
    cinn = copy(inn)
    cinn[inn > 9] = 0
    return cinn


def run_gen(inn, n_gens=1):
    out_3 = inn
    n_flashes = 0
    for _ in range(n_gens):
        out_1 = step1(out_3)
        (out_2, n_flashes_this_round) = step2(out_1)
        n_flashes += n_flashes_this_round
        out_3 = step3(out_2)
    return out_3, n_flashes


def find_sync(inn, safety=10000):
    out_3 = inn
    n_rounds = 0
    for _ in range(safety):
        out_1 = step1(out_3)
        (out_2, n_flashes_this_round) = step2(out_1)
        out_3 = step3(out_2)
        n_rounds += 1
        if np.all(out_3 == out_3[0, 0]):
            return n_rounds


inn = parse_input(puzzle_input)
gen1, n_flashes = run_gen(inn)
print(np.all(gen1 == gen1_sol))
gen2, n_flashes = run_gen(inn, 100)
print(f"{np.all(gen2 == gen2_sol)} {n_flashes}")
print(find_sync(inn))

gen1_sol = parse_input(
    [
        "6594254334",
        "3856965822",
        "6375667284",
        "7252447257",
        "7468496589",
        "5278635756",
        "3287952832",
        "7993992245",
        "5957959665",
        "6394862637",
    ]
)
gen1_sol
gen2_sol = parse_input(
    [
        "8807476555",
        "5089087054",
        "8597889608",
        "8485769600",
        "8700908800",
        "6600088989",
        "6800005943",
        "0000007456",
        "9000000876",
        "8700006848",
    ]
)
