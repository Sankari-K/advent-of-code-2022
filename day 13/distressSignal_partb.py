from ast import literal_eval
from functools import cmp_to_key

def parse():
    res = []
    first = input()
    while first:
        res.append(first)
        res.append(input())
        input() # ignoring newline
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

def day13_partb(packets):
    packets.append('[[2]]')
    packets.append('[[6]]')

    for index, packet in enumerate(packets):
        packets[index] = literal_eval(packet)

    packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

packets = parse()
print(day13_partb(packets))