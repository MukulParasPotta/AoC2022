from io import TextIOWrapper
from string import ascii_uppercase
from string import ascii_lowercase
from itertools import islice

priority_sum = 0
with open('input.txt', 'r') as input:
    lines = input.readlines()
    size = len(lines)
    chunks = 0
    while chunks < size:
        slice = lines[chunks:chunks+3]
        chunks+=3
        slice = [set(line.strip()) for line in slice]
        common_element = list(slice[0].intersection(slice[1].intersection(slice[2])))[0]
        position_upper = ascii_uppercase.find(common_element)
        position_lower = ascii_lowercase.find(common_element)
        if position_upper != -1:
            priority_sum += (27 + position_upper)
        else:
            priority_sum += (1 + position_lower)
    print(priority_sum)
