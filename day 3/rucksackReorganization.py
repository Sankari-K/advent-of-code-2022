PRIORITY = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 
    'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 
    'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 
    'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 
    'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 
    'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

def day3_parta():
    priorities = 0
    while True:
        inp = input()
        if inp == "q":
            break
        firstCompartment, secondCompartment = set(inp[:len(inp) // 2]), set(inp[len(inp) // 2:])
        (item,) = firstCompartment.intersection(secondCompartment)
        priorities += PRIORITY[item]
    return priorities

def day3_partb():
    priorities = 0
    while True:
        first = input()
        if not first:
            break
        second = input()
        third = input()

        first, second, third = set(first), set(second), set(third)
        item = first.intersection(second)
        (item, ) = item.intersection(third)
        priorities += PRIORITY[item]
    return priorities


print(day3_partb())
