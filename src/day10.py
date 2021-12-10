#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np
import statistics
from itertools import permutations
from itertools import count
from functools import reduce
from copy import copy
from copy import deepcopy


puzzle_input = get_puzzle_data(day=10)
example_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]
legal_first = {"[": "]", "(": ")", "{": "}", "<": ">"}
dual_dict = {val: key for (key, val) in legal_first.items()}
for (key, val) in copy(dual_dict).items():
    dual_dict[val] = key

scores_first = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores_second = {"(": 1, "[": 2, "{": 3, "<": 4}


def update_score(score, cha):
    return score * 5 + scores_second[cha]


class TheStacks:
    def __init__(self):
        self.stack = []
        self.illegals = {"}": 0, "]": 0, ")": 0, ">": 0}
        self.first_illegal = ""

    def append(self, cha):
        # is cha an opener?
        if cha in legal_first:
            self.stack.append(cha)
        else:
            # if not, need to modify the stack
            stack_var = self.stack.pop()
            if not (stack_var == dual_dict[cha]):
                self.illegals[cha] += 1
                if not self.first_illegal:
                    self.first_illegal = cha

    def close(self):
        this_score = 0
        tmp_ex = copy(self.stack)
        for _ in range(len(self.stack)):
            cha = self.stack.pop()
            this_score = update_score(this_score, cha)
        return this_score


list_of_illegals = []
cha_added = []
for line in puzzle_input:
    s = TheStacks()
    for cha in line:
        s.append(cha)
    if s.first_illegal:
        # the corrupt lines
        list_of_illegals.append(s.first_illegal)
    else:
        # the incomplete lines
        cha_added.append(s.close())

print(sorted(cha_added)[2 + (len(cha_added) // 2)])
