def day4_parta():
    pairs = 0
    while True:
        inp = input()
        if inp == "q":
            break
        first, second = inp.split(",")

        first = getRange(first)
        second = getRange(second)
        
        if second[0] >= first[0] and second[1] <= first[1]:
            pairs += 1
        elif first[0] >= second[0] and first[1] <= second[1]:
            pairs += 1
        
    return pairs

def day4_partb():
    pairs = 0
    while True:
        inp = input()
        if inp == "q":
            break

        first, second = inp.split(",")
        first = getRange(first)
        second = getRange(second)
        
        if not (first[1] < second[0] or second[1] < first[0]):
            pairs += 1
    return pairs

def getRange(interval):
    start, stop = map(int, interval.split("-"))
    return [start, stop]

"""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
print(day4_partb())