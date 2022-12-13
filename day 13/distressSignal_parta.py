from ast import literal_eval

def parse():
    res = []
    first = input()
    while first:
        second = input()
        res.append([first, second])
        input()  # for the newline
        first = input()
    return res

def compare(a, b):
    # returns 1 if a < b, 0 if a == b, -1 if a > b
    if type(a) == type(b) == int:
        if a < b:
            return 1
        if a == b:
            return 0
        return -1

    elif type(a) == type(b) == list:
        min_length = min(len(a), len(b))
        for index in range(min_length):
            ele_a = a[index]
            ele_b = b[index]
            if compare(ele_a, ele_b) == 1:
                return 1
            if compare(ele_a, ele_b) == -1:
                return -1
        
        if len(a) == len(b):
            return 0
        if len(a) < len(b):
            return 1
        return -1
    else:
        if type(a) == int:
            a = [a]
        else:
            b = [b]
        return compare(a, b)

def day13_parta(packets):
    correct_order = 0
    for index, packet in enumerate(packets):
        left, right = packet
        left = literal_eval(left)
        right = literal_eval(right)
        if compare(left, right) == 1:
            correct_order += index + 1
    return correct_order

packets = parse()
print(day13_parta(packets))
