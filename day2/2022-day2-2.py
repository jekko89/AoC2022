file = open('input.txt')

"""
A = Rock = 1
B = Paper = 2
C = Scissors = 3

X = lose
Y = draw
Z = win

Lose += 0
Draw += 3
Win += 6
"""

def result_wanted(self):
    if self == 'X':
        return 0
    if self == 'Y':
        return 3
    if self == 'Z':
        return 6

def rps_compare(opponent, result):
    if opponent == 'A':
        if result == 'X':
            return 3
        if result == 'Y':
            return 1
        if result == 'Z':
            return 2
    if opponent == 'B':
        if result == 'X':
            return 1
        if result == 'Y':
            return 2
        if result == 'Z':
            return 3
    if opponent == 'C':
        if result == 'X':
            return 2
        if result == 'Y':
            return 3
        if result == 'Z':
            return 1


total = 0
self_value = 0
for line in file.readlines():
    line = line.split(" ")
    line[1] = line[1].strip()
    self_value = rps_compare(line[0], line[1])
    result = result_wanted(line[1])
    total += self_value + result

print(total)
