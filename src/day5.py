#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np

puzzle_input = get_puzzle_data(day=5)
example_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]
inn = example_input


def process_input(inn):
    [[list(map(int, y.split(","))) for y in x.split(" -> ")] for x in inn]
    points = np.zeros(shape=(len(inn), 2, 2), dtype=int)

    for (i_point, pointer) in enumerate(inn):
        processed_pointer = [
            list(map(int, y.split(","))) for y in pointer.split(" -> ")
        ]
        points[i_point, :, :] = processed_pointer
    return points


# points varies by set x (start,stop) x (x,y)


def get_x(points):
    matches = points[:, 0, 1] == points[:, 1, 1]
    return points[matches, :, :]


def get_y(points):
    matches = points[:, 0, 0] == points[:, 1, 0]
    return points[matches, :, :]


def get_diagonal(points):
    neither_matches = np.logical_not(
        (points[:, 0, 0] == points[:, 1, 0]) | (points[:, 0, 1] == points[:, 1, 1])
    )
    return points[neither_matches, :, :]


def update_x_lines(line_matrix, points):
    for point in points:
        from_p, to_p = (min(point[:, 0]), max(point[:, 0]))
        y = point[0, 1]
        line_matrix[y, range(from_p, to_p + 1)] += 1


def update_y_lines(line_matrix, points):
    for point in points:
        from_p, to_p = (min(point[:, 1]), max(point[:, 1]))
        x = point[0, 0]
        line_matrix[range(from_p, to_p + 1), x] += 1


def update_diag_lines(line_matrix, points):
    for point in points:
        from_x, to_x = point[:, 0]
        if from_x > to_x:
            to_x -= 1
            sign_x = -1
        else:
            to_x += 1
            sign_x = 1

        from_y, to_y = point[:, 1]
        if from_y > to_y:
            to_y -= 1
            sign_y = -1
        else:
            to_y += 1
            sign_y = 1

        line_matrix[range(from_y, to_y, sign_y), range(from_x, to_x, sign_x)] += 1


points = process_input(puzzle_input)
x_points = get_x(points)
y_points = get_y(points)
diag_points = get_diagonal(points)

max_shape = points.max() + 1
line_count = np.zeros(shape=(max_shape, max_shape), dtype=int)
update_x_lines(line_count, x_points)
update_y_lines(line_count, y_points)

print(np.sum(line_count >= 2))


# problem 2
update_diag_lines(line_count, diag_points)

print(np.sum(line_count >= 2))


if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    bin_array = np.zeros(shape=(len(puzzle_input), len(puzzle_input[0])), dtype="bool")
    print(f"{count_increase(sea_depths)}")
