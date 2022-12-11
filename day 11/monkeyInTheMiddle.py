import parser
import functools

class Monkey:
    def __init__(self, id, items, operation, test_number, throw_to):
        self.id = id # to identify a monkey
        self.items = items # list of items currently with monkey
        self.items_handled = 0 # total items handled over all rounds

        self.operation = operation 
        self.test_number = test_number
        self.throw_to = throw_to # list of monkeys to which it throws
        
    def simulate_turn(self, modulo):
        while self.items:
            self.items_handled += 1
            worry_level = self.apply_operation(self.items[0], modulo)
            self.pass_to_monkey(worry_level)
            self.items = self.items[1:]

    def apply_operation(self, item, modulo):
        formula = self.operation
        code = parser.expr(formula).compile()
        old = item
        if modulo == 3:
            return eval(code) // modulo
        else:
            return eval(code) % modulo

    def pass_to_monkey(self, item):
        if item % self.test_number == 0:
            MONKEYS[self.throw_to[0]].insert(item)
        else:
            MONKEYS[self.throw_to[1]].insert(item)

    def insert(self, item):
        self.items.append(item)


def parseInput():
    inp = input() # this always gets us the id
    MONKEYS = []
    while inp:
        id = int(inp.split()[-1][:-1])
        starting_items = (input().split(":")[-1]).split(", ")
        starting_items = list(map(lambda x: int(x.strip()), starting_items))
        operation = input().split("=")[-1][1:]
        test_number = int(input().split()[-1])
        throw_to = [int(input().split()[-1]), int(input().split()[-1])]

        monkey = Monkey(id, starting_items, operation, test_number, throw_to)
        MONKEYS.append(monkey)

        input() # the blank line, ignore
        inp = input() # id for next monkey

    return MONKEYS

def day11(MONKEYS, rounds):
    if rounds == 20:
        modulo = 3
    else:
        divisors = [monkey.test_number for monkey in MONKEYS]
        modulo = functools.reduce(lambda a, b: a * b, divisors)
    for _ in range(rounds):
        for monkey in MONKEYS:
            monkey.simulate_turn(modulo)
    
    number_of_inspects = sorted([i.items_handled for i in MONKEYS], reverse=True)
    return number_of_inspects[0] * number_of_inspects[1]
    
MONKEYS = parseInput()
# print(day11(MONKEYS, 20))  # part one
print(day11(MONKEYS, 10000)) # part two




