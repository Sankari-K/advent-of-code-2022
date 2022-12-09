def day4_parta(intervals):
    pairs = 0
    for interval in intervals:
        first, second = interval
        first = getRange(first)
        second = getRange(second)
        
        if second[0] >= first[0] and second[1] <= first[1]:
            pairs += 1
        elif first[0] >= second[0] and first[1] <= second[1]:
            pairs += 1
    return pairs

def day4_partb(intervals):
    pairs = 0
    for interval in intervals:
        first, second = interval
        first = getRange(first)
        second = getRange(second)
        
        if not (first[1] < second[0] or second[1] < first[0]):
            pairs += 1
    return pairs

def parse():
    intervals = []
    inp = input()
    while inp:
        intervals.append(inp.split(","))
        inp = input()
    return intervals

def getRange(interval):
    start, stop = map(int, interval.split("-"))
    return [start, stop]

interval = parse()
print(day4_parta(interval))
print(day4_partb(interval))