stacks = []
with open('input.txt') as input:
    line = input.readline()
    while line[1] != '1':
        line = ''.join(ele if idx % 4 == 1 else '' for idx, ele in enumerate(line))
        if len(stacks) == 0:
            stacks = [[] for _ in range(len(line))]
        for idx, crate in enumerate(line):
            if crate != ' ':
                stacks[idx].append(crate)
        line = input.readline()
    for idx in range(len(stacks)):
        stacks[idx] = stacks[idx][::-1]
    
    line = input.readline()
    line = input.readline()
    while line != '':
        split = line.split()
        count, src, dest = int(split[1]), int(split[3]), int(split[5])
        for _ in range(count):
            stacks[dest-1].append(stacks[src-1].pop())
        line = input.readline()
    print(''.join(stack[-1] for stack in stacks))