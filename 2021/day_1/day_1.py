#!/usr/bin/env python3

# https://adventofcode.com/2021/day/1

import os
import more_itertools as mit

# Resolve input file path
fp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "day_1-data_input-mei.txt")

# Save each line into a variable
with open (fp) as file_object:
    data = [int(line.rstrip()) for line in file_object]

def is_increased(first: int, second: int) -> int:
    if second > first:
        return 1
    else:
        return 0

sum_of_increased=0
overlapping_chunks = list(mit.windowed(data, n=2, step=1))
for c in overlapping_chunks:
    sum_of_increased+=is_increased(*c)
print(sum_of_increased)