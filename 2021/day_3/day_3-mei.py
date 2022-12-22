#!/usr/bin/env python3

from collections import Counter
import os

# https://adventofcode.com/2021/day/2


## Part 1.
# Resolve input file path
fp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "day_3-data_input-mei.txt")

# Read all the lines in the file and remove trailing white space
with open (fp) as file_object:
    data = [line.rstrip() for line in file_object]


def get_decimal(binary_string: str) -> int:
    return int(binary_string, base=2)


def get_common(lst: list, freq='high') -> str:
    c = Counter(lst)
    if freq == 'high':
        return max(lst, key=c.get)
    elif freq == 'low':
        return min(lst, key=c.get)
    else:
        return f'{freq} is not an argument'

zipped_list = list(zip(*data))

epsilon = ''
gamma = ''
for pairs in zipped_list:
    gamma+=get_common(lst=pairs,freq='high')
    epsilon+=get_common(lst=pairs, freq='low')

gamma = get_decimal(gamma)
epsilon = get_decimal(epsilon)

print(gamma * epsilon)