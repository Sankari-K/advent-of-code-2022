def day5_parta():
    crates = {1: ["B", "L", "D", "T", "W", "C", "F", "M"],
              2: ["N", "B", "L"],
              3: ["J", "C", "H", "T", "L", "V"],
              4: ["S", "P", "J", "W"],
              5: ["Z", "S", "C", "F", "T", "L", "R"],
              6: ["W", "D", "G", "B", "H", "N", "Z"],
              7: ["F", "M", "S", "P", "V", "G", "C", "N"],
              8: ["W", "Q", "R", "J", "F", "V", "C", "Z"],
              9: ["R", "P", "M", "L", "H"]}

    # crates = {1: ["Z", "N"],
    #           2: ["M", "C", "D"],
    #           3: ["P"]}

    while True:
        inp = input()
        if inp == "q":
            break
        _, qty, _, source, _, destination = inp.split()

        qty, source, destination = map(int, [qty, source, destination])

        for _ in range(qty):
            crates[destination].append(crates[source].pop())

    top = ""
    for value in crates.values():
        top += value[-1]
    return top

def day5_partb():
    crates = {1: ["B", "L", "D", "T", "W", "C", "F", "M"],
              2: ["N", "B", "L"],
              3: ["J", "C", "H", "T", "L", "V"],
              4: ["S", "P", "J", "W"],
              5: ["Z", "S", "C", "F", "T", "L", "R"],
              6: ["W", "D", "G", "B", "H", "N", "Z"],
              7: ["F", "M", "S", "P", "V", "G", "C", "N"],
              8: ["W", "Q", "R", "J", "F", "V", "C", "Z"],
              9: ["R", "P", "M", "L", "H"]}

    # crates = {1: ["Z", "N"],
    #           2: ["M", "C", "D"],
    #           3: ["P"]}

    while True:
        inp = input()
        if inp == "q":
            break
        _, qty, _, source, _, destination = inp.split()

        qty, source, destination = map(int, [qty, source, destination])

        crates[destination] += crates[source][-1 * qty:]
        crates[source] = crates[source][: -1 * qty]

    top = ""
    for value in crates.values():
        top += value[-1]
    return top

print(day5_parta())