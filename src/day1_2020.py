#!/usr/bin/env python3

from src.shared import get_puzzle_data
from src.shared import post_answer

puzzle_input = get_puzzle_data(day=1, year=2020)
tps_reports = [int(x) for x in puzzle_input]

net_product = 0
for (ii, entry_one) in enumerate(tps_reports):
    for entry_two in tps_reports[ii:]:
        if entry_one + entry_two == 2020:
            net_product = entry_one * entry_two

post_answer(net_product, 1, 1, 2020)

net_three_product = 0
for (ii, entry_one) in enumerate(tps_reports):
    for (jj, entry_two) in enumerate(tps_reports[ii:]):
        for entry_three in tps_reports[jj:]:
            if entry_one + entry_two + entry_three == 2020:
                net_three_product = entry_one * entry_two * entry_three


post_answer(net_three_product, 2, 1, 2020)

if __name__ == "__main__":
    puzzle_input = get_puzzle_data(day=1)
    sea_depths = [int(x) for x in puzzle_input]
    print(f"{count_increase(sea_depths)}")
