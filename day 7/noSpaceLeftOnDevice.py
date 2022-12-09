class Node(object):
    def __init__(self, val="", parent=None):
        self.val = val
        self.neighbours = []
        self.weight = 0
        self.parent = parent


def parse():
    file = Node("/", None)
    current = file
    inp = input()

    while inp:
        inp = inp.split()

        if inp[0] == "$" and inp[1] == "cd":
            if inp[2] == "/":
                current = file
            elif inp[2] == "..":
                print(current)
                current = current.parent
            else:
                for neighbour in current.neighbours:
                    if neighbour.val == inp[2]:
                        current = neighbour
        elif inp[0] != "$":
            new = Node(inp[1], current)
            new.weight = 0 if inp[0] == "dir" else int(inp[0])
            current.neighbours.append(new)
        inp = input()

    return file

def findSum(dir, ALL_DIRS):
    tot = 0
    for neighbour in dir.neighbours:
        if neighbour.weight == 0:
            neighbour.weight = findSum(neighbour, ALL_DIRS)
        tot += neighbour.weight
    ALL_DIRS.append(tot)
    return tot
        
def dfs(dir):
    res = 0
    if dir.neighbours != [] and dir.weight <= 100000: # it is a folder
        res += dir.weight
    for neighbour in dir.neighbours:
        res += dfs(neighbour)
    return res

def day7(file):
    ALL_DIRS = []
    findSum(file, ALL_DIRS)

    unused_space = 70000000 - max(ALL_DIRS)
    space_reqd = 30000000 - unused_space
    ALL_DIRS = filter(lambda x: x >= space_reqd, ALL_DIRS)
    ALL_DIRS = sorted(ALL_DIRS)
     
    # return [ans_for_part_a, ans_for_part_b]
    return [dfs(file), ALL_DIRS[0]]

file = parse()
print(day7(file))




