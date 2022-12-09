import copy 

def stackParser():
    # get line by line and add to a 2d list
    stacks = []
    inp = input()
    while inp:
        stacks.append(inp)
        inp = input()
    # transpose
    stacks = list(zip(*stacks))

    # remove noise
    new_stack = []
    for line in stacks:
        new_line = list(filter(lambda x: x not in "[ ]", line))
        if new_line:
            new_stack.append("".join(new_line))

    # create a dict
    stacks = dict()
    for stack in new_stack:
        stacks[int(stack[-1])] = list(stack[:-1][::-1])
    return stacks

def instructionParser():
    instructions = []
    inp = input()
    while inp:
        _, qty, _, source, _, destination = inp.split()
        qty, source, destination = map(int, [qty, source, destination])
        instructions.append([qty, source, destination])
        inp = input()
    return instructions
    
def day5_parta(crates, instructions):
    for instruction in instructions:
        qty, source, destination = instruction
        for _ in range(qty):
            crates[destination].append(crates[source].pop())

    top = ""
    for value in crates.values():
        top += value[-1]
    return top

def day5_partb(crates, instructions):
    for instruction in instructions:
        qty, source, destination = instruction
        crates[destination] += crates[source][-1 * qty:]
        crates[source] = crates[source][: -1 * qty]
    
    top = ""
    for value in crates.values():
        top += value[-1]
    return top

crates = stackParser()
new_crates = copy.deepcopy(crates)
instructions = instructionParser()

print(day5_parta(crates, instructions))
print(day5_partb(new_crates, instructions))