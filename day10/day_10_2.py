positions_list = [20, 60, 100, 140, 180, 220]
def check_sprite(clock, x_value):
    mod = (clock % 40)
    return x_value - 1 <= mod and mod <= x_value + 1

with open('input.txt') as input:
    clock_cycles = 0
    x_value = 1
    pixels = [' ' for _ in range(241)]
    for line in input.readlines():
        split = line.strip().split()
        if check_sprite(clock_cycles, x_value):
            pixels[clock_cycles] = '#'
        clock_cycles += 1
        if len(split) == 2:
            if check_sprite(clock_cycles, x_value):
                pixels[clock_cycles] = '#'
            clock_cycles += 1
            x_value += int(split[1])
    for i in range(0, 240, 40):
        print(''.join(pixels[i:i+40]))