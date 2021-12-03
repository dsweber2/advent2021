#!/usr/bin/env python3
import json
import requests
from pathlib import Path

root_path = Path(__file__).parents[1]
config = json.load(root_path.joinpath("config.json").open())


def download_puzzle_data(year, day):
    """Fetch puzzle input data from AoC, using the cookie value stored in config.json"""
    print(f"Fetching puzzle input for day {day}")
    res = requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": config["aoc_cookie"]},
    )
    res.raise_for_status()
    with open(root_path.joinpath("data", f"year{year}/day{day}_input.txt"), "w") as fp:
        fp.write(res.text)


def get_puzzle_data(filename=None, day=None, year=config["year"]):
    """Retrieve puzzle data locally (if already downloaded) or invokes download_puzzle_data()"""
    if filename:
        day = int(filename.split("/")[-1][3:5])
    if not day:
        raise ValueError("get_puzzle_data() must be called with either filename or day")
    puzzle_input = root_path.joinpath("data", f"year{year}/day{day}_input.txt")
    if not puzzle_input.exists():
        download_puzzle_data(year, day)

    return puzzle_input.open().read().splitlines()


def post_answer(ans, level, day, year=config["year"]):
    requests.post(
        f"https://adventofcode.com/{year}/day/{day}/11/answer",
        cookies={"session": config["aoc_cookie"]},
        headers={"User-Agent": "dsweber2",},
        data={"level": f"{level}", "answer": f"{ans}"},
    )
