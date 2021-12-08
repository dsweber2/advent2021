#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np
import statistics
from itertools import permutations
from itertools import count
from copy import copy

puzzle_input = get_puzzle_data(day=8)
example_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]
letters_to_numbers = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def process_input(inn):
    return [[x.split() for x in ex.split(" | ")] for ex in inn]


parsed = process_input(puzzle_input)

base_letters = "abcdefg"


def apply_map(string, mapping):
    new_string = ""
    for cha in string:
        new_string += base_letters[mapping.index(cha)]
    return new_string


def check_valid(string):
    return "".join(sorted(string)) in letters_to_numbers


def get_this_map(example):
    for mapping in permutations("abcdefg"):
        remapped = [apply_map(x, mapping) for x in example]
        all_valids = [check_valid(x) for x in remapped]
        if all(all_valids):
            return mapping
        elif any(all_valids):
            # print(f"{[''.join(sorted(string)) for string in remapped]},   {all_valids}")
            3
    return -1


example = just_output[1][0]
correct_map = get_this_map(just_output[1])


def convert_to_int(example, correct_map):
    remapped = "".join(sorted(apply_map(example, correct_map)))
    return letters_to_numbers[remapped]


def count_output_digits(parsed):
    just_output = [ex[1] for ex in parsed]
    correct_maps = [get_this_map(output) for output in just_output]
    output_ints = [
        [convert_to_int(output, correct_maps[ii]) for output in just_output[ii]]
        for ii in range(len(just_output))
    ]
    return np.sum(
        np.array([[out.count(ii) for ii in range(9)] for out in output_ints]), axis=0
    )


def form_numbers(parsed):
    all_exs = [x[0] + x[1] for x in parsed]
    just_output = [ex[1] for ex in parsed]
    correct_maps = [get_this_map(output) for output in all_exs]
    output_ints = [
        [convert_to_int(output, correct_maps[ii]) for output in just_output[ii]]
        for ii in range(len(just_output))
    ]
    return np.array(output_ints).dot([10 ** (3 - ii) for ii in range(4)])


n_digits = count_output_digits(parsed)
print(np.sum(n_digits[[1, 4, 7, 8]]))
print(np.sum(n_digits))

the_numbers = form_numbers(parsed)
print(the_numbers)
print(np.sum(the_numbers))

if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    bin_array = np.zeros(shape=(len(puzzle_input), len(puzzle_input[0])), dtype="bool")
    print(f"{count_increase(sea_depths)}")
