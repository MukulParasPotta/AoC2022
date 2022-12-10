from bisect import bisect_left
with open('input.txt') as input:
    stack = []
    sizes_list = []
    for line in input.readlines():
        line = line.strip()
        split = line.split()
        if split[0] == '$':
            if split[1] == 'cd':
                if split[2] == '..':
                    s = stack.pop()
                    sizes_list.append(s)
                    stack[-1] += s
                    continue
                stack.append(0)
        if split[0][0].isdigit():
            stack[-1] += int(split[0])
    while len(stack) != 1:
        s = stack.pop()
        sizes_list.append(s)
        stack[-1] += s
    sizes_list.append(stack[0])
    sizes_list.sort()
    free_space = 70000000 - sizes_list[-1]
    needed_to_clear = 30000000 - free_space
    print(sizes_list[bisect_left(sizes_list, needed_to_clear)])

    