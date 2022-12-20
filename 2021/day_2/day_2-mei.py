#!/usr/bin/env python3

# https://adventofcode.com/2021/day/2

import csv
import os
from collections import Counter

# Resolve input file path
fp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "day_2-data_input-mei.txt")

nav_entries = []

with open(fp, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ')
    for row in data:
        nav_entries.append((row[0], int(row[1])))

def get_part_1(tuple_list: list) -> int:
    d = {}
    for entry, num in tuple_list:
        d[entry] = d.get(entry, 0) + num
    d['depth'] = d['down'] - d['up']
    return d['forward'] * d['depth']

print(get_part_1(tuple_list=nav_entries))

def get_part_2(tuple_list: list) -> int:
    horizontal_pos=0
    aim=0
    depth=0

    for item in tuple_list:
        if item[0] == 'down':
            aim+=item[1]
        elif item[0] == 'up':
            aim-=item[1]
        elif item[0] == 'forward':
            horizontal_pos+=item[1]
            depth+=aim*item[1]
    return horizontal_pos * depth

print(get_part_2(tuple_list=nav_entries))