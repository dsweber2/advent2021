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


def single_convert(hex_int):
    raw_bin = bin(int(hex_int, 16))[2:]
    extras = "0" * ((-len(raw_bin)) % 4)
    return extras + raw_bin


def process_input(inn):
    return reduce(lambda a, b: a + b, map(single_convert, inn))


class packet:
    def __init__(self, header, packet_version, packet_id, data):
        self.header = header
        self.version = packet_version
        self.id = packet_id
        self.data = data

    def __repr__(self):
        """pretty printing that shows the given expressions"""
        if self.id == 4:
            # literal returns the value
            return f"{self.data}"

        subreps = [f"{pac}" for pac in self.data]
        if self.id == 0:
            # 0 is just a sum
            return " + ".join(subreps)
        elif self.id == 1:
            # 1 is just a product
            return " * ".join(subreps)
        elif self.id == 2:
            # 2 is just a minimum
            return "min(" + ", ".join(subreps) + ")"
        elif self.id == 3:
            # 3 is just a maximum
            return "max(" + ", ".join(subreps) + ")"
        elif self.id == 5:
            # 5 is a comparator that returns true if the first value is larger
            return subreps[0] + " < " + subreps[1]
        elif self.id == 6:
            # 6 is a comparator that returns true if the second value is larger
            return subreps[0] + " > " + subreps[1]
        elif self.id == 7:
            # 7 is a comparator that returns true if the values are equal
            return subreps[0] + " == " + subreps[1]

        return f"(h={self.header}, v={self.version}, id={self.id}, data={self.data})"

    def execute(self):
        if self.id == 4:
            # literal returns the value
            return self.data
        elif self.id == 0:
            # 0 is just a sum
            return sum([pac.execute() for pac in self.data])
        elif self.id == 1:
            # 1 is just a product
            return reduce(lambda x, y: x * y, [pac.execute() for pac in self.data])
        elif self.id == 2:
            # 2 is just a minimum
            return min([pac.execute() for pac in self.data])
        elif self.id == 3:
            # 3 is just a maximum
            return max([pac.execute() for pac in self.data])
        elif self.id == 5:
            # 5 is a comparator that returns true if the first value is larger
            return 1 * (self.data[0].execute() > self.data[1].execute())
        elif self.id == 6:
            # 6 is a comparator that returns true if the second value is larger
            return 1 * (self.data[0].execute() < self.data[1].execute())
        elif self.id == 7:
            # 7 is a comparator that returns true if the values are equal
            return 1 * (self.data[0].execute() == self.data[1].execute())


def process_literal(string):
    next_word = string[6:11]
    words = [next_word[1:]]
    ind = 1
    while next_word[0] == "1":
        next_word = string[(6 + ind * 5) : (6 + (ind + 1) * 5)]
        words.append(next_word[1:])
        ind += 1
    words = int("".join(words), 2)
    net_ind = 6 + ind * 5
    mod4 = 0  # (4 - net_ind) % 4
    remainder = string[net_ind + mod4 :]
    return remainder, words


def process_operation_total_length(string):
    length = int(string[7:22], 2)
    if length != len(string[22 : (22 + length)]):
        print(string)
        print(length)
        print(string[22 : (22 + length)])
        print("lengths don't match!")
        raise InterruptedError()
    remainder, words, version_sum = break_packet(string[22 : (22 + length)], 0)
    # NOT DONE
    return string[(22 + length) :], words, version_sum


def process_operation_n_packets(string):
    n_packets = int(string[7:18], 2)
    remainder, sub_packets, version_sum = break_packet(string[18:], 0, n_packets)

    return remainder, sub_packets, version_sum


def is_zeros(string):
    return all([x == "0" for x in string])


def break_packet(string, version_sum, n_packets=-1):
    # base case: an empty string
    if string == "" or is_zeros(string):
        return ("", [], version_sum)
    header = string[:6]
    packet_version = int(header[:3], 2)
    packet_id = int(header[3:], 2)
    if packet_id == 4:
        remainder, words = process_literal(string)
    else:
        type_id = string[6]
        if type_id == "0":
            remainder, words, extra_version_sum = process_operation_total_length(string)
            version_sum += extra_version_sum
        else:
            remainder, words, extra_version_sum = process_operation_n_packets(string)
            version_sum += extra_version_sum
    pac = packet(header, packet_version, packet_id, words)
    version_sum += packet_version

    if n_packets > 1:
        # add another packet to the list of packets associated with an operator
        remainder, other_packets, version_sum = break_packet(
            remainder, version_sum, n_packets - 1
        )
        return remainder, [pac] + other_packets, version_sum
    elif n_packets == 1:
        other_packets = []  # finally reached the end of the line
        return remainder, [pac], version_sum
    elif n_packets <= 0:
        # not inside of an operator at all, so use the default n_packets
        remainder, other_packets, version_sum = break_packet(remainder, version_sum)
        return remainder, [pac] + other_packets, version_sum


puzzle_input = get_puzzle_data(day=16)
example_input = [
    "D2FE28",
    "38006F45291200",
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
    "C200B40A82",
    "04005AC33890",
    "880086C3E88112",
    "CE00C43D881120",
    "D8005AC2A8F0",
    "F600BC2D8F",
    "9C005AC2F8F0",
    "9C0141080250320F1802104A08",
]

ii = 7
other_string = process_input(example_input[ii])  # 6
string, packets, version_sum = break_packet(other_string, 0)
print(example_input[ii])
print(version_sum)
print(packets)
print(packets[0].execute())

bin_string = process_input(puzzle_input[0])

# string, packets, version_sum = break_packet(other_string, 0)

string, packets, version_sum = break_packet(bin_string, 0)
print(version_sum)
print(packets)
print(packets[0].execute())
