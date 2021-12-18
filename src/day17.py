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
import importlib
import time
import sys
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

import numpy as np


def process_input(inn):
    raw_bin = bin(int(inn, 16))[2:]
    extras = "0" * ((-len(raw_bin)) % 4)
    return extras + raw_bin


puzzle_input = get_puzzle_data(day=17)
example_input = ["target area: x=20..30, y=-10..-5"]


class probe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = x
        self.vy = y

    def update_position(self):
        self.x += self.vx
        self.y += self.vy
        self.vx = min(self.vx - 1, 0)
        self.vy -= 1


# x gives the number of rounds
#
def velocity_to_end_position(vx, vy):
    x = vx * (vx + 1) / 2
    y = vy * vx - x


def valid_vxs(lower, upper):
    vx = 0
    valid_vx = []
    while vx < lower:
        x = vx * (vx + 1) / 2
        if (x > lower) & (x < upper):
            valid_vx.append(vx)

        vx += 1
    return valid_vx


vxs = valid_vxs(20, 30)


import argparse
import importlib
import time
import sys
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

import numpy as np


class AdventProblem(ABC):
    """
    An abstraction of an advent code problem.
    """

    def __init__(self, name: str):
        """
        :param name: a name useful for logging and debugging
        """

        self.name = name

    @abstractmethod
    def solve_part1(self) -> str:
        """
        Solve the advent problem part 1.
        """

    @abstractmethod
    def solve_part2(self) -> str:
        """
        Solve the advent problem part 2.
        """


class Day17(AdventProblem):
    def __init__(self, test: bool):
        super().__init__("Trick shot")
        target_file = "day17_test.txt" if test else "day17_target.txt"
        target_area = open(target_file, "r").readlines()[0].strip()
        print(target_area.split("target area: x="))
        _, xy_range = target_area.split("target area: x=")
        x_range, y_range = xy_range.split(", y=")
        x_lower, x_upper = x_range.split("..")
        y_lower, y_upper = y_range.split("..")
        self.x_range = (int(x_lower), int(x_upper))
        self.y_range = (int(y_lower), int(y_upper))
        print(f"x_range: {self.x_range}")
        print(f"y_range: {self.y_range}")

    def valid_vxs(self) -> Tuple[int, int]:
        lower, upper = self.x_range
        vx = 0
        for vx in range(lower + 1):
            x = vx * (vx + 1) / 2
            if lower < x < upper:
                min_vx = vx
                break

        max_vx = upper + 1  # guaranteed to be too fast
        return (min_vx - 1, max_vx)

    def valid_vys(self):
        lower, upper = self.y_range
        return 0, max(abs(lower), abs(upper)) + 2

    def ends_in_target(self, vx_: int, vy_: int) -> Tuple[bool, int]:
        vx, vy = vx_, vy_
        impossibru = False
        x, y = 0, 0
        xstart, xend = self.x_range
        ystart, yend = self.y_range
        max_y = -np.inf
        n_its = 0
        while not impossibru:
            x += vx
            y += vy

            # print(f'x,y: {x,y} (vx,vy: {vx,vy}')
            if n_its > 100:
                sys.exit(-1)
            max_y = max(max_y, y)
            if y == 0:
                print(f"Now at zero: {x},{y}, {vx},{vy} ({vx_}, {vy_})")
            if xstart <= x <= xend and ystart <= y <= yend:
                return True, max_y

            vx = max(vx - 1, 0)
            vy -= 1
            n_its += 1

            if x > xend or y < ystart:
                # print("Its impossibru!!!!")
                impossibru = True
        return False, max_y

    def solve_part1(self) -> str:
        min_vx, max_vx = self.valid_vxs()
        max_y = -np.inf
        min_vy, max_vy = self.valid_vys()
        print(f"vy range: {min_vy, max_vy}")
        print(f"vx range: {min_vx, max_vx}")
        for vy in range(min_vy, max_vy):
            for vx in range(min_vx, max_vx):
                valid, potent_max_y = self.ends_in_target(vx, vy)
                if valid:
                    print(f"potent_max_y is: {potent_max_y} for vx,vy {vx},{vy}")
                    if potent_max_y > max_y:
                        max_y = potent_max_y

        return f"{max_y}"

    def solve_part2(self) -> str:
        return f""


def run_day(day: int, test: bool) -> None:
    module = importlib.import_module("main")
    class_ = getattr(module, f"Day{day}")
    time1 = time.time()
    instance: AdventProblem = class_(test)
    time2 = time.time()
    print(f"Creating the class took {time2 - time1:.4f} seconds")
    print(f'Now solving Day {day} "{instance.name}":')
    part1, time3 = instance.solve_part1(), time.time()
    print(f"Part 1 ({time3 - time2:.4f} s) - {part1}")
    part2, time4 = instance.solve_part2(), time.time()
    print(f"Part 2 ({time4 - time3:.4f} s) - {part2}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("main.py")

    parser.add_argument(dest="day", help="which day to run")
    parser.add_argument(
        "-t",
        "--test",
        dest="test",
        help="run the output on the test data",
        action="store_true",
    )
    parser.set_defaults(test=False)

    args = parser.parse_args()

    run_day(args.day, args.test)
