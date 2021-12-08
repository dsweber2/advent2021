#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np

puzzle_input = get_puzzle_data(day=6)
example_input = ["3,4,3,1,2"]
inn = example_input


def process_input(inn):
    return list(map(int, inn[0].split(",")))


class lanternFish:
    fish_pop = np.zeros(shape=8, dtype=int)
    new_age = 8
    veteran_age = 6
    day = 0

    def __init__(self, init_dist, new_age=8, veteran_age=6, day=0):
        self.fish_pop = np.zeros(shape=(new_age + 1,), dtype=int)
        for fish in init_dist:
            self.fish_pop[fish] += 1
        self.new_age = new_age
        self.veteran_age = veteran_age
        self.day = day

    def day(self, n_days=1):
        for _ in range(n_days):
            # how many new fish
            new_fish = self.fish_pop[0]
            # age the fish
            self.fish_pop[:-1] = self.fish_pop[1:]
            self.fish_pop[-1] = 0
            self.fish_pop[self.new_age] += new_fish
            self.fish_pop[self.veteran_age] += new_fish
        self.day += n_days

    def count(self):
        return self.fish_pop.sum()


s = example_input[0]
gen = (int(x) for x in s.split(","))


def f():
    for x in s.split(","):
        yield x


init_dist = process_input(example_input)
l = lantern_fish(init_dist)
print(l.fish_pop)
l.pass_day(n_days=80)
print(l.count())
print(l.day)


init_dist = process_input(puzzle_input)
l = lantern_fish(init_dist)
l.pass_day(n_days=80)

init_dist = process_input(puzzle_input)
l = lantern_fish(init_dist)
l.pass_day(n_days=256)

if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    bin_array = np.zeros(shape=(len(puzzle_input), len(puzzle_input[0])), dtype="bool")
    print(f"{count_increase(sea_depths)}")
