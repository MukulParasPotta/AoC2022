with open('input.txt') as input:
    elves = []
    temp = 0
    for line in input.readlines():
        if len(line.strip()) != 0:
            temp += int(line.strip())
        else:
            elves.append(temp)
            temp = 0
    elves.sort()
    print(elves[-1])
    print(sum(elves[-3:]))