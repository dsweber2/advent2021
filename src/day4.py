#!/usr/bin/env python3

from src.shared import get_puzzle_data
import numpy as np

puzzle_input = get_puzzle_data(day=4)
example_input = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    " 8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    " 2  0 12  3  7",
]
inn = example_input

puzzle_input[0].split()

card_size = 5


def process_input(inn, card_size=5):
    called_nums = [int(x) for x in inn[0].split(",")]
    n_cards = int((len(inn) - 1) / 6)
    cards = np.zeros((card_size, card_size, n_cards), dtype=int)
    for ii in range(n_cards):
        tokens = np.array(
            [
                [int(x) for x in row.split()]
                for row in inn[(2 + 6 * ii) : (1 + 6 * (ii + 1))]
            ]
        )
        cards[:, :, ii] = tokens
    return cards, called_nums


def check_win(boards, card_size=5):
    check_vertical = np.sum(boards, axis=0) == card_size
    check_horizontal = np.sum(boards, axis=1) == card_size
    did_board_x_win = np.any(check_vertical, axis=0) + np.any(check_horizontal, axis=0)
    return did_board_x_win


def get_score(cards, has_been_called, board):
    return np.sum(np.sum(np.logical_not(has_been_called) * cards, axis=0), axis=0)[
        board
    ]


def problem1(inn):
    cards, called_nums = process_input(inn)

    has_been_called = cards == called_nums[0]
    any_won = check_win(has_been_called)
    if any(any_won):
        which_won = np.argmax(any_won)
        get_score(cards, has_been_called, which_won)

    final_score = 0
    for num in called_nums[1:]:
        print(num)
        has_been_called = (cards == num) | has_been_called
        any_won = check_win(has_been_called)
        if any(any_won):
            which_won = np.argmax(any_won)
            final_score = get_score(cards, has_been_called, which_won) * num
            break
    print(final_score)
    return final_score


problem1(puzzle_input)


def problem2(inn):
    cards, called_nums = process_input(inn)

    has_been_called = cards == called_nums[0]
    any_won = check_win(has_been_called)
    has_won_yet = np.zeros(shape=any_won.shape, dtype=bool)
    if all(any_won):
        which_won = np.argmax(any_won)
        get_score(cards, has_been_called, which_won)

    final_score = 0
    for num in called_nums[1:]:
        print(num)
        has_been_called = (cards == num) | has_been_called
        any_won = check_win(has_been_called)
        if all(any_won):
            which_won = np.argmin(has_won_yet)
            print(which_won)
            final_score = get_score(cards, has_been_called, which_won) * num
            break
        has_won_yet = has_won_yet | any_won
    print(final_score)
    return final_score


problem2(example_input)
problem2(puzzle_input)


if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    bin_array = np.zeros(shape=(len(puzzle_input), len(puzzle_input[0])), dtype="bool")
    print(f"{count_increase(sea_depths)}")
