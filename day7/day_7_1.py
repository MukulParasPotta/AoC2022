with open('input.txt') as input:
    stack = []
    total = 0
    for line in input.readlines():
        line = line.strip()
        split = line.split()
        if split[0] == '$':
            if split[1] == 'cd':
                if split[2] == '..':
                    s = stack.pop()
                    if s <= 100000:
                        total += s
                    stack[-1] += s
                    continue
                stack.append(0)
        if split[0][0].isdigit():
            stack[-1] += int(split[0])
    while len(stack) != 1:
        s = stack.pop()
        stack[-1] += s
    if stack[0] <= 100000:
        total += stack[0]
    print(total)
