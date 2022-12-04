count_1 = 0
count_2 = 0
with open('input.txt') as input:
    for line in input.readlines():
        line = line.strip()
        pair1, pair2 = [list(map(int, pair.split('-'))) for pair in line.split(',')]
        if (pair1[0] <= pair2[0] and pair1[1] >= pair2[1]) or (pair1[0] >= pair2[0] and pair1[1] <= pair2[1]):
            count_1 += 1
        if ((pair1[0] <= pair2[0] and pair1[1] >= pair2[0]) or (pair1[0] >= pair2[0] and pair1[0] <= pair2[1])):
            count_2 += 1
    print(count_1)
    print(count_2)