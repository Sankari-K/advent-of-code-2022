def parse():
    program = []
    inp = input()
    hash = 0
    while inp:
        for _ in range(len(inp.split())):
            program.append(str(hash) + inp)
        inp = input()
        hash += 1
    return program

def day10_parta(instructions):
    clock = 1
    register_value = 1
    signal_strength_sum = 0

    REQD_CYCLES = [20, 60, 100, 140, 180, 220]
    for index, instruction in enumerate(instructions):
        if clock in REQD_CYCLES:
            # print(clock * register_value, register_value)
            signal_strength_sum += clock * register_value
        clock += 1
        
        if index != 0 and len(instruction.split()) == 2 and instructions[index - 1] == instruction:
            register_value += int(instruction.split()[-1])
    return signal_strength_sum

def day10_partb(instructions):
    clock = 0
    register_value = 1
    crt_row = []
    answer = []
    for index, instruction in enumerate(instructions):
        sprite_values = (register_value - 1, register_value, register_value + 1)
        if clock in sprite_values:
            crt_row.append("#")
        else:
            crt_row.append(".")
        clock = (clock + 1) % 40

        if len(crt_row) == 40:
            answer.append("".join(crt_row))
            crt_row = []

        if index != 0 and len(instruction.split()) == 2 and instructions[index - 1] == instruction:
            register_value += int(instruction.split()[-1])

    return answer


instructions = parse()
print(day10_parta(instructions))
print("\n".join(day10_partb(instructions)))