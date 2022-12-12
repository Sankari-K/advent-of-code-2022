from collections import deque

HEIGHT = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 
          'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 
          'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 
          'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
HEIGHT["S"] = 0
HEIGHT["E"] = 25

def parse():
    map = []
    inp = input()
    while inp:
        if "S" in inp:
            source = (len(map), inp.index("S"))
        if "E" in inp:
            destination = (len(map), inp.index("E"))
        map.append(list(inp))
        inp = input()
    return map, source, destination

def day12(source, destination, part):
    queue = deque()
    visited = set()

    visited.add(destination)
    queue.append((destination, 0))

    while len(queue) > 0:
        element, distance = queue.popleft()
        prev_height = HEIGHT[MAP[element[0]][element[1]]]

        if element == source and part == "a": # part a
             return distance

        if MAP[element[0]][element[1]] in "aS" and part == "b": # part b
            return distance

        if ((element[0] + 1, element[1]) not in visited and 
            element[0] + 1 not in [-1, MAX_X] and element[1] not in [-1, MAX_Y] and 
            prev_height - HEIGHT[MAP[element[0] + 1][element[1]]] <= 1):

            visited.add((element[0] + 1, element[1]))
            queue.append(((element[0] + 1, element[1]), distance + 1))

        if ((element[0] - 1, element[1]) not in visited and 
            element[0] - 1 not in [-1, MAX_X] and element[1] not in [-1, MAX_Y] and 
            prev_height - HEIGHT[MAP[element[0] - 1][element[1]]] <= 1):  

            visited.add((element[0] - 1, element[1]))
            queue.append(((element[0] - 1, element[1]), distance + 1))

        if ((element[0], element[1] + 1) not in visited and 
            element[0] not in [-1, MAX_X] and element[1] + 1 not in [-1, MAX_Y] and 
            prev_height - HEIGHT[MAP[element[0]][element[1] + 1]] <= 1):    

            visited.add((element[0], element[1] + 1))
            queue.append(((element[0], element[1] + 1), distance + 1))

        if ((element[0], element[1] - 1) not in visited and 
            element[0] not in [-1, MAX_X] and element[1] - 1 not in [-1, MAX_Y] and 
            prev_height - HEIGHT[MAP[element[0]][element[1] - 1]] <= 1):   

            visited.add((element[0], element[1] - 1))
            queue.append(((element[0], element[1] - 1), distance + 1))

MAP, source, destination = parse()
MAX_X = len(MAP)
MAX_Y = len(MAP[0])
print(day12(source, destination, "a")) # part a
print(day12(source, destination, "b")) # part b


