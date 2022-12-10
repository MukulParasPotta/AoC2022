import numpy as np
with open('input.txt') as input:
    forest = []
    for line in input.readlines():
        forest.append(list(map(int, list(line.strip()))))
    size = len(forest)
    visible = [[False for i in range(size)] for j in range(size)] 
    for i in range(size):
        visible[i][0] = True
        visible[i][size-1] = True
        visible[size-1][i] = True
        visible[0][i] = True
    count = 0
    forest = np.array(forest, dtype=np.int)
    for i in range(size):
        for j in range(size):
            if not ((i == 0 or i == size - 1) or (j == 0 or j == size - 1)):
                slicex1 = max(forest[i, :j])
                slicex2 = max(forest[i, j+1:])
                slicey1 = max(forest[:i, j])
                slicey2 = max(forest[i+1:, j])
                visible[i][j] = forest[i][j] > min(slicex1, slicex2, slicey1, slicey2)
            if visible[i][j]:
                count += 1
    print(count)
    