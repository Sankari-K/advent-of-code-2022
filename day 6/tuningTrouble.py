def getInput():
    s = input()
    return s


def day6(datastream, DISTINCT_CHARS):
    from collections import deque

    current_index = DISTINCT_CHARS
    q = deque(datastream[:DISTINCT_CHARS])

    markers = DISTINCT_CHARS
    while len(set(q)) != DISTINCT_CHARS:
        q.popleft()
        markers += 1
        q.append(datastream[current_index])
        current_index += 1
    
    return markers

print(day6(getInput(), 4))
print(day6(getInput(), 14))



    
