#!/usr/bin/env python3

from shared import get_puzzle_data
import numpy as np
import statistics
from itertools import permutations
from itertools import count
from functools import reduce
from copy import copy
from copy import deepcopy


puzzle_input = get_puzzle_data(day=13)
example_input = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]


def parse_input(inn):
    indices = []
    folds = []
    maxes = [0, 0]
    for line in inn:
        if len(line) == 0:
            pass
        elif line[0] == "f":
            folds.append(parse_folds(line))
        else:
            indices.append([int(x) for x in line.split(",")])
            maxes = [max(maxes[0], indices[-1][0]), max(maxes[1], indices[-1][1])]
    contains_mark = np.zeros(shape=1 + np.array([2000, 2000]), dtype=bool)
    for ind in indices:
        contains_mark[ind[0], ind[1]] = True
    return folds, contains_mark


def parse_folds(string):
    real = string.split()[-1]
    xy, num = real.split("=")
    if xy == "x":
        return [int(num), 0]
    else:
        return [0, int(num)]


def fold(bool_mat, fold_ind):
    if fold_ind[0] == 0:
        # fold first dimension
        new_mat = (
            bool_mat[:, (2 * fold_ind[1]) : (fold_ind[1]) : -1]
            | bool_mat[:, 0 : fold_ind[1]]
        )
    else:
        new_mat = (
            bool_mat[(2 * fold_ind[0]) : (fold_ind[0]) : -1, :]
            | bool_mat[0 : fold_ind[0], :]
        )

    return new_mat


folds
# print(np.array(contains_mark, dtype=int).T)
folds, contains_mark = parse_input(puzzle_input)

for fold_ind in folds:
    print(fold_ind)
    contains_mark = fold(contains_mark, fold_ind)

print(np.array(contains_mark, dtype=int).T)
contains_mark
