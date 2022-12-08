def parse():
    forest = []
    while True:
        inp = input()
        if inp == "q":
            break
        line = list(map(int, inp))
        forest.append(line)
    return forest

def dfs_a(x, y):
    answer = [True, True, True, True]
    # check top
    offset = 1
    while x - offset >= 0:
        if FOREST[x - offset][y] >= FOREST[x][y]:
            answer[0] = False
            break
        offset += 1
        
    # check bottom 
    offset = 1
    while x + offset <= MAX_X - 1:
        if FOREST[x + offset][y] >= FOREST[x][y]:
            answer[1] = False
            break
        offset += 1
    
    # check left
    offset = 1
    while y - offset >= 0:
        if FOREST[x][y - offset] >= FOREST[x][y]:
            answer[2] = False
            break
        offset += 1

    # check right
    offset = 1
    while y + offset <= MAX_Y - 1:
        if FOREST[x][y + offset] >= FOREST[x][y]:
            answer[3] = False
            break
        offset += 1
    return any(answer)

def dfs_b(x, y):
    if x in [0, MAX_X - 1] or y in [0, MAX_Y - 1]:
        return 0
    scenic_cover = 1

    # check top
    offset = 1
    while x - offset > 0:
        if FOREST[x - offset][y] >= FOREST[x][y]:
            break
        offset += 1
    print(offset)
    scenic_cover *= offset
 
    # check bottom 
    offset = 1
    while x + offset < MAX_X - 1:
        if FOREST[x + offset][y] >= FOREST[x][y]:
            break
        offset += 1
    print(offset)
    scenic_cover *= offset

    # check left
    offset = 1
    while y - offset > 0:
        if FOREST[x][y - offset] >= FOREST[x][y]:
            break
        offset += 1
    print(offset)
    scenic_cover *= offset

    # check right
    offset = 1
    while y + offset < MAX_Y - 1:
        if FOREST[x][y + offset] >= FOREST[x][y]:
            break
        offset += 1
    print(offset)
    scenic_cover *= offset

    return scenic_cover

def day8_parta(forest):
    visible = 0
    for x_index, line in enumerate(forest):
        for y_index, tree in enumerate(line):
            if dfs_a(x_index, y_index):
                visible += 1
    return visible

def day8_partb(forest):
    max_cover = 0
    for x_index, line in enumerate(forest):
        for y_index, tree in enumerate(line):
            max_cover = max(dfs_b(x_index, y_index), max_cover)
            print(x_index, y_index, dfs_b(x_index, y_index))
    return max_cover


FOREST = parse()

MAX_X = len(FOREST)
MAX_Y = len(FOREST[0])

# print(day8_parta(FOREST))
print(day8_partb(FOREST))

