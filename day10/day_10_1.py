positions_list = [20, 60, 100, 140, 180, 220]
def check_clock(clock):
    return clock in positions_list

with open('input.txt') as input:
    clock_cycles = 0
    x_value = 1
    score = 0
    for line in input.readlines():
        split = line.strip().split()
        clock_cycles += 1
        if check_clock(clock_cycles):
            score += clock_cycles * x_value
        if len(split) == 2:
            clock_cycles += 1
            if check_clock(clock_cycles):
                score += clock_cycles * x_value
            x_value += int(split[1])
    print(score)