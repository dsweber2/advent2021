#!/usr/bin/env python3

from shared import get_puzzle_data
import numpy as np
import statistics
from itertools import permutations
from itertools import count
from functools import reduce
from copy import copy
from copy import deepcopy
import heapq as h


puzzle_input = get_puzzle_data(day=15)
example_input = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]


def parse_input(inn):
    return np.array([[int(string) for string in line] for line in inn])


class node:
    def __init__(self, location, cost_mat):
        self.l = location
        self.parent_mat = cost_mat.view()

    def __repr__(self):
        return f"{self.l, self.get_val()}"

    def get_val(self):
        return self.parent_mat[self.l[0], self.l[1]]

    def __eq__(self, other):
        return self.get_val() == other.get_val()

    def __lt__(self, other):
        return self.get_val() < other.get_val()


class PathFinder:
    # self.cost_array
    # self.actual_cost
    # self.visited
    # self.heap

    def __init__(self, cost_array, actual_cost=None):
        if actual_cost == None:
            actual_cost = np.infty * np.ones(shape=cost_array.shape, dtype=int)
            actual_cost[0, 0] = 0
        self.cost_array = cost_array
        self.actual_cost = actual_cost
        self.visited = np.zeros(shape=cost_array.shape, dtype=bool)
        self.heap = [node((0, 0), self.actual_cost)]

    def __repr__(self):
        return f"Costs:\n{self.actual_cost}\nHeap:\n{self.heap}"

    def is_complete(self):
        return self.actual_cost[-1, -1] < np.infty

    def check_in_bounds(self, ind):
        if (ind[0] < 0) | (ind[0] >= self.cost_array.shape[0]):
            return False
        if (ind[1] < 0) | (ind[1] >= self.cost_array.shape[1]):
            return False
        return True

    def update_cost(self, n, current_cost):
        potential_cost = current_cost + self.cost_array[n[0], n[1]]
        if potential_cost < self.actual_cost[n[0], n[1]]:
            self.actual_cost[n[0], n[1]] = potential_cost
            return potential_cost
        else:
            return self.actual_cost[n[0], n[1]]

    def add_neighbors(self, ind):
        y, x = ind
        neighbors = [
            [y + 1, x],
            [y, x + 1],
            [y - 1, x],
            [y, x - 1],
        ]
        current_cost = self.actual_cost[ind[0], ind[1]]

        in_bound = [n for n in neighbors if self.check_in_bounds(n)]
        in_bound = [n for n in in_bound if (not self.visited[n[0], n[1]])]

        for ii in range(len(in_bound)):
            self.update_cost(in_bound[ii], current_cost)
            h.heappush(self.heap, node(in_bound[ii], self.actual_cost))

    def pop(self):
        best = h.heappop(self.heap)
        self.visited[best.l[0], best.l[1]] = True
        self.add_neighbors(best.l)


cost_array = parse_input(puzzle_input)
actual_cost = np.infty * np.ones(shape=cost_array.shape, dtype=int)


p = PathFinder(cost_array)
print(p)
while True:
    p.pop()
    if p.is_complete():
        print(p)
        break
