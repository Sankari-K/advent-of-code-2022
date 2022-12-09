def day2_parta(inp):
    score = 0
    weights = {"X": 1, "Y":2, "Z": 3}
    correspondance = {"X": "A", "Y":"B", "Z": "C"}

    for line in inp:
        opp, me = line
        score += weights[me]
        if correspondance[me] == opp:
            score += 3 # draw
        elif me == "X":
            if opp == "C":
                score += 6
        elif me == "Y":
            if opp == "A":
                score += 6
        else:
            if opp == "B":
                score += 6
    return score

def day2_partb(inp):
    score = 0
    for line in inp:
        opp, result = line
        results = {"X": 0, "Y": 3, "Z": 6}
        signs = {"A": 1, "B": 2, "C": 3}
        score += results[result]
        if result == "X": # need to lose
            if opp == "A":
                score += 3
            elif opp == "B":
                score += 1
            else:
                score += 2
        elif result == "Y": # need to draw
            score += signs[opp]
        else:
            if opp == "A":
                score += 2
            elif opp == "B":
                score += 3
            else:
                score += 1
    return score

def parse():
    res = []
    inp = input()
    while inp:
        res.append(inp.split())
        inp = input()
    return res

inp = parse()

print(day2_parta(inp))
print(day2_partb(inp))