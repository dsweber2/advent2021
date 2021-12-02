#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np
import String

puzzle_input = get_puzzle_data(day=2)
separated = [x.split(" ") for x in puzzle_input]


def get_depth_length(separated):
    horizontal = 0
    vertical = 0
    for x in separated:
        if x[0] == "forward":
            horizontal += int(x[1])
        elif x[0] == "down":
            vertical += int(x[1])
        elif x[0] == "up":
            vertical -= int(x[1])
    return horizontal * vertical


print(f"{get_depth_length(separated)}")


def get_depth_length_aim(separated):
    horizontal = 0
    vertical = 0
    aim = 0
    for x in separated:
        dist = int(x[1])
        if x[0] == "forward":
            horizontal += dist
            vertical += dist * aim
        elif x[0] == "down":
            aim += dist
        elif x[0] == "up":
            aim -= dist
    return horizontal * vertical


if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    sea_depths = [int(x) for x in puzzle_input]
    print(f"{count_increase(sea_depths)}")
