from typing import List, Tuple
from copy import deepcopy

class Monkey:
    def __init__(self, items, update, test, decision) -> None:
        self.items = items
        self.update = update
        self.test = test
        self.decision = decision
        self.activity = 0
    
    def get_activity(self):
        return self.activity

    def update_tension(self, manageable=False) -> None:
        for i in range(len(self.items)):
            if self.update[1] != 'old':
                if self.update[0] == '+':
                    self.items[i] += self.update[1]
                if self.update[0] == '*':
                    self.items[i] *= self.update[1]
            else:
                if self.update[0] == '+':
                    self.items[i] += self.items[i]
                if self.update[0] == '*':
                    self.items[i] *= self.items[i]
            if manageable:
                self.items[i] //= 3
            else:
                self.items[i] %= modulo
    
    def throw_items(self, manageable) -> List[Tuple]:
        self.update_tension(manageable)
        self.activity += len(self.items)
        decisions = []
        for item in self.items:
            if item % self.test == 0:
                decisions.append((item, self.decision[0]))
            else:
                decisions.append((item, self.decision[1]))
        self.items = []
        return decisions

    def __str__(self) -> str:
        return f'{self.items}\n{self.update}\n{self.test}\n{self.decision}\n'

def solve(monkeys: List, rounds, manageable):
    for _ in range(rounds):
        for monkey in monkeys:
            for item, monkey_idx in monkey.throw_items(manageable):
                monkeys[monkey_idx].items.append(item)
    monkeys.sort(key=lambda x: x.get_activity())
    print(monkeys[-1].get_activity() * monkeys[-2].get_activity())

modulo = 0

def get_modulo(monkeys):
    value = 1
    for monkey in monkeys:
        value *= monkey.test
    return value

with open('input.txt') as input:
    monkeys = []
    items = []
    update = []
    test = 0
    decisions = []
    for idx, line in enumerate(input.readlines()):
        i = idx % 7
        if i in [1,2,3,4,5]:
            if i == 1:
                items = list(map(int, line.strip().split(':')[1].strip().split(',')))
            if i == 2:
                update = line.strip().split(':')[1].split()[-2:]
                if update[1].isnumeric():
                    update[1] = int(update[1])
            if i == 3:
                test = int(line.strip().split(':')[1].split()[-1])
            if i == 4 or i == 5:
                decisions.append(int(line.strip().split(':')[1].split()[-1]))
        if i == 6:
            monkeys.append(Monkey(deepcopy(items), deepcopy(update), int(test), deepcopy(decisions)))
            decisions.clear()
    modulo = get_modulo(monkeys)
    monkeys2 = deepcopy(monkeys)
    solve(monkeys, 20, True)
    solve(monkeys2, 10000, False)