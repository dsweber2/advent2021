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


def process_input(inn):
    raw_bin = bin(int(inn, 16))[2:]
    extras = "0" * ((-len(raw_bin)) % 4)
    return extras + raw_bin


class packet:
    def __init__(self, header, packet_version, packet_id, data):
        self.header = header
        self.version = packet_version
        self.id = packet_id
        self.data = data

    def __repr__(self):
        return f"(h={self.header}, v={self.version}, id={self.id}, data={self.data})"


def process_literal(string):
    ind = 0
    next_word = string[(6 + ind * 5) : (6 + (ind + 1) * 5)]
    words = [next_word[1:]]
    while next_word[0] == "1":
        next_word = string[(6 + ind * 5) : (6 + (ind + 1) * 5)]
        words.append(next_word[1:])
        print(next_word)
        ind += 1
    net_ind = 6 + (1 + ind) * 5
    mod4 = (net_ind + 1) % 4
    remainder = string[net_ind + mod4 :]
    return remainder, words


def process_operation_total_length(string):
    length = int(string[7:22], 2)
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

    if n_packets > 0:
        # add another packet to the list of packets associated with an operator
        remainder, other_packets, version_sum = break_packet(
            remainder, version_sum, n_packets - 1
        )
        return remainder, [pac] + other_packets, version_sum
    elif n_packets == 0:
        other_packets = []  # finally reached the end of the line
        return remainder, [pac], version_sum
    elif n_packets < 0:
        # not inside of an operator at all, so use the default n_packets
        remainder, other_packets, version_sum = break_packet(remainder, version_sum)
        return remainder, [pac] + other_packets, version_sum


puzzle_input = get_puzzle_data(day=16)
example_input = ["8A004A801A8002F478", "620080001611562C8802118E34"]
inn = puzzle_input[0]


bin_string = process_input(puzzle_input[0])
other_string = process_input(example_input[0])

# string, packets, version_sum = break_packet(other_string, 0)

string, packets, version_sum = break_packet(bin_string, 0)
