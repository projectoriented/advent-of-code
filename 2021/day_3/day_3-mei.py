#!/usr/bin/env python3

from collections import Counter
import os
import functools

# https://adventofcode.com/2021/day/3


## Part 1.
# Resolve input file path
fp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "day_3-data_input-mei.txt")

# Read all the lines in the file and remove trailing white space
with open (fp) as file_object:
    data = [line.rstrip() for line in file_object]


def get_decimal(binary_string: str) -> int:
    """
    Convert a binary string to decimal.
    Args:
        binary_string (str): binary string

    Returns:
        int: decimal of binary string
    """
    return int(binary_string, base=2)


def get_common(lst: list, freq: str) -> str:
    """
    Get most/least common bit.

    Args:
        lst (list): A list of bit strings.
        freq (str): Desired frequency, e.g. high or low

    Returns:
        str: The most/least common bit string in the list.
    """
    c = Counter(lst)
    equal_freq = functools.reduce(lambda x, y: x == y, c.values())
    
    if equal_freq == True:
        if freq == 'high':
            return '1'
        elif freq == 'low':
            return '0'
    else:
        if freq == 'high':
            return max(lst, key=c.get)
        elif freq == 'low':
            return min(lst, key=c.get)

# Group the positional bits in each byte.
positional_bits_lst = list(zip(*data))

def get_consumption_rate(lst: list) -> int:
    epsilon = ''
    gamma = ''
    for bits in lst:
        gamma+=get_common(lst=bits,freq='high')
        epsilon+=get_common(lst=bits, freq='low')

    gamma = get_decimal(gamma)
    epsilon = get_decimal(epsilon)

    return gamma * epsilon

## Part 2.
        