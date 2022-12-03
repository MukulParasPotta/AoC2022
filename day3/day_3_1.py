from string import ascii_uppercase
from string import ascii_lowercase

priority_sum = 0
with open('input.txt') as input:
    for line in input.readlines():
        line = line.strip()
        length = len(line)
        compartments = set(line[:length//2]), set(line[length//2:])
        common_element = list(compartments[0].intersection(compartments[1]))[0]
        position_upper = ascii_uppercase.find(common_element)
        position_lower = ascii_lowercase.find(common_element)
        if position_upper != -1:
            priority_sum += (27 + position_upper)
        else:
            priority_sum += (1 + position_lower)
    print(priority_sum)