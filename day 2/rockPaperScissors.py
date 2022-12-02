def day2_parta():
    score = 0
    weights = {"X": 1, "Y":2, "Z": 3}
    correspondance = {"X": "A", "Y":"B", "Z": "C"}

    while True:
        inp = input()
        if inp == "q":
            break
        opp, me = inp.split()
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

def day2_partb():
    score = 0
    while True:
        inp = input()
        if inp == "q":
            break
        opp, result = inp.split()
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


print(day2_partb())