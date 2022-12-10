import numpy as np

def find_view_distance(slice, height, reverse=False):
    if reverse:
        slice = slice[::-1]
    pos = 0
    for h in slice:
        if h < height: pos += 1
        if h >= height:
            pos += 1
            break
    return pos

with open('input.txt') as input:
    forest = []
    for line in input.readlines():
        forest.append(list(map(int, list(line.strip()))))
    size = len(forest)
    score = 0
    forest = np.array(forest, dtype=np.int)
    for i in range(size):
        for j in range(size):
            if not ((i == 0 or i == size - 1) or (j == 0 or j == size - 1)):
                slicex1 = find_view_distance(forest[i, :j], forest[i][j], True)
                slicex2 = find_view_distance(forest[i, j+1:], forest[i][j])
                slicey1 = find_view_distance(forest[:i, j], forest[i][j], True)
                slicey2 = find_view_distance(forest[i+1:, j], forest[i][j])
                score = max(score, slicex1 * slicex2 * slicey1 * slicey2)
    print(score)
    