#!/usr/bin/env python3

from shared import get_puzzle_data
import numpy as np
import statistics
from itertools import permutations
from itertools import count
from functools import reduce
from copy import copy
from copy import deepcopy


puzzle_input = get_puzzle_data(day=14)
example_input = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]


def parse_input(inn):
    pair_to_extra = {}
    for x in inn[2:]:
        pair, out = x.split(" -> ")
        pair_to_extra[pair] = pair[0] + out
    return (inn[0], pair_to_extra)


inn, pair_to_extra = parse_input(puzzle_input)


def insert(inn, pair_to_extra):
    exploded = [inn[ii : (ii + 2)] for ii in range(len(inn))]
    for (ii, x) in enumerate(exploded):
        if x in pair_to_extra:
            exploded[ii] = pair_to_extra[x]
    return "".join(exploded)


test = insert(inn, pair_to_extra)
test = copy(inn)
for _ in range(10):
    test = insert(test, pair_to_extra)

uniques = set(test)
counts = []
for c in uniques:
    counts.append(test.count(c))
print(max(counts) - min(counts))


def add_default_(dic, el, amount=1):
    dic[el] = dic.get(el, 0) + amount


def sparser_input(inn):
    pair_to_extra = {}
    for x in inn[2:]:
        pair, out = x.split(" -> ")
        pair_to_extra[pair] = [pair[0] + out, out + pair[1]]
    sparse_rep = {}
    letter_count = {}
    init = inn[0]
    for ii in range(len(init)):
        if ii < len(init) - 1:
            add_default_(sparse_rep, init[ii : (ii + 2)], 1)
        c = init[ii]
        letter_count[c] = letter_count.get(c, 0) + 1
    return (letter_count, sparse_rep, pair_to_extra)


def update_tuple(in_pair, n, sparse_rep, letter_count, pair_to_extra):
    if (in_pair in pair_to_extra) & (n > 0):
        sparse_rep[in_pair] -= n
        new_pairs = pair_to_extra[in_pair]
        cha = new_pairs[0][1]
        add_default_(letter_count, cha, n)
        for new_pair in new_pairs:
            add_default_(sparse_rep, new_pair, n)


def update_round(letter_count, sparse_rep, pair_to_extra):
    spare_rep = deepcopy(sparse_rep)
    for pair in spare_rep:
        n = spare_rep[pair]
        update_tuple(pair, n, sparse_rep, letter_count, pair_to_extra)


letter_count, sparse_rep, pair_to_extra = sparser_input(puzzle_input)
for _ in range(40):
    update_round(letter_count, sparse_rep, pair_to_extra)


print(max(letter_count.values()) - min(letter_count.values()))
