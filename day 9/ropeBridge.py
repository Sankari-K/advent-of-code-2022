def is_touching(head_pos, tail_pos):
    # overlapping
    if head_pos == tail_pos:
        return True
    # adjacent 
    if head_pos[0] == tail_pos[0]:
        return abs(head_pos[1] - tail_pos[1]) == 1
    if head_pos[1] == tail_pos[1]:
        return abs(head_pos[0] - tail_pos[0]) == 1
    # diagonally adjacent
    if abs(head_pos[0] - tail_pos[0]) == 1 and abs(head_pos[1] - tail_pos[1]) == 1:
        return True
    return False

def update_tail(first_part, second_part):
    # head is two steps directly L or R
    if first_part[0] == second_part[0]:
        diff = first_part[1] - second_part[1]
        second_part[1] += 1 if diff > 0 else -1
        
    # head is two steps directly U or D
    elif first_part[1] == second_part[1]:
        diff = first_part[0] - second_part[0]
        second_part[0] += 1 if diff > 0 else -1
    else:
        tmp = second_part.copy()
        if is_touching(first_part, [second_part[0] + 1, second_part[1] + 1]):
            second_part = [tmp[0] + 1, tmp[1] + 1]
        elif is_touching(first_part, [second_part[0] - 1, second_part[1] - 1]):
            second_part = [tmp[0] - 1, tmp[1] - 1]
        elif is_touching(first_part, [second_part[0] + 1, second_part[1] - 1]):
            second_part = [tmp[0] + 1, tmp[1] - 1]
        elif is_touching(first_part, [second_part[0] - 1, second_part[1] + 1]):
            second_part = [tmp[0] - 1, tmp[1] + 1]
 
    return second_part

def parse():
    instructions = []
    inp = input()
    while inp:
        instructions.append(inp.split())
        inp = input()
    return instructions

def day9(moves, knots):
    visited = set()
    visited.add((0, 0))

    # this list would contain positions of all parts of the rope
    POSITIONS = [[0,0] for _ in range(knots)]

    for move in moves:
        direction, step = move
        step = int(step)
        for s in range(step):
            if direction == "R":
                POSITIONS[0][1] += 1
            if direction == "L":
                POSITIONS[0][1] -= 1
            if direction == "U":
                POSITIONS[0][0] += 1
            if direction == "D":
                POSITIONS[0][0] -= 1

            for first_index in range(knots - 1):
                first_part = POSITIONS[first_index]
                second_part = POSITIONS[first_index + 1]
                if not is_touching(first_part, second_part):
                    POSITIONS[first_index + 1] = update_tail(first_part, second_part)
                    
            visited.add(tuple(POSITIONS[-1]))
    return len(visited)

moves = parse()
print(day9(moves, 2))
print(day9(moves, 10))

    