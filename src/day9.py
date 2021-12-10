#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np
import statistics
from itertools import permutations
from itertools import count
from copy import copy

puzzle_input = get_puzzle_data(day=9)
example_input = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]
inn = example_input
print([int(char) for char in inn[0]])


def process_input(inn) -> np.array:
    return np.array([[int(char) for char in row] for row in inn])


def find_derivatives(vals) -> (np.array, np.array):
    return np.diff(vals, axis=0), np.diff(vals, axis=1)


def pad_with_true(mat, before, axis=0):
    if axis == 0:
        trues = np.ones(shape=(1, mat.shape[1]), dtype=bool)
    elif axis == 1:
        trues = np.ones(shape=(mat.shape[0], 1), dtype=bool)
    else:
        raise ("can't be bothered")
    if before:
        return np.concatenate((trues, mat), axis=axis)
    else:
        return np.concatenate((mat, trues), axis=axis)


vals = process_input(example_input)
dy, dx = find_derivatives(vals)

print(dx)
pos_x = pad_with_true(dx > 0, False, 1)  # is it increasing going to the right?
pos_y = pad_with_true(dy > 0, False, 0)
neg_x = pad_with_true(dx < 0, True, 1)  # is it decreasing coming from the left?
neg_y = pad_with_true(dy < 0, True, 0)  # is it decreasing coming from above?
is_minima = pos_x & pos_y & neg_x & neg_y
print(np.sum(vals[is_minima] + 1))

to_the_nines = vals == 9
mins = np.where(is_minima)
start_locs = [np.array(x) for x in zip(mins[0], mins[1])]

[1,2,3].index(3)
class Node:
    location = (0, 0)
    traversed_edges = {
        np.array([-1, 0]): False,
        np.array([1, 0]): False,
        np.array([0, -1]): False,
        np.array([0, 1]): False,
    }

    def __init__(self, loc, parent, otherPossible):
        self.location = loc
        parent_edge = (parent.location - loc)
        self.traversed_edges[parent_edge] = True
        for neighbor in traversed_edges:
            if otherPossible. neighbor
        return
    def __eq__(self, other : Node):
        return self.location == other.location


def add_points(boundary, list_of_interior, edge_set):
    """a search algorithm to find all connected components in the graph. `boundary` is a binary matrix listing wether a node is impassible. `list_of_interior` is the points with no possible neighbors left"""
    maxes = 3
    for x in edge_set:
        if x[0]:
            3


if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    bin_array = np.zeros(shape=(len(puzzle_input), len(puzzle_input[0])), dtype="bool")
    print(f"{count_increase(sea_depths)}")
