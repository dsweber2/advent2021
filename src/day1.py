#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np

puzzle_input = get_puzzle_data(day=1)
sea_depths = [int(x) for x in puzzle_input]

sea_depth_list = sea_depths


def count_increase(sea_depth_list):
    """solution to the first problem, counting the total number of times the input increases"""
    previous_depth = sea_depth_list[0]
    total_increased = 0
    for depth in sea_depth_list:
        if previous_depth < depth:
            total_increased += 1
        previous_depth = depth
    return total_increased


print(f"{count_increase(sea_depths)}")


def smooth_and_count(sea_depth_list, window_size):
    windowing = window_size * [1]
    smoothed = np.convolve(windowing, sea_depth_list)
    return count_increase(smoothed[2:-2])


# test example
print(f"{smooth_and_count([199, 200, 208, 210, 200, 207, 240, 269, 260, 263],3)}")
print(f"{smooth_and_count(sea_depths,3)}")


if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    sea_depths = [int(x) for x in puzzle_input]
    print(f"{count_increase(sea_depths)}")
