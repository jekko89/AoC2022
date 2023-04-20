file = open('input.txt')

"""
A = Rock
B = Paper
C = Scissors

X = Rock = 1
Y = Paper = 2
C = Scissors = 3

Lose += 0
Draw += 3
Win += 6
"""

def user_guess(self):
    if line[1] == 'X':
        return 1
    if line[1] == 'Y':
        return 2
    if line[1] == 'Z':
        return 3

def rps_compare(opponent, self):
    if opponent == 'A':
        if self == 'X':
            return 3
        if self == 'Y':
            return 6
        if self == 'Z':
            return 0
    if opponent == 'B':
        if self == 'X':
            return 0
        if self == 'Y':
            return 3
        if self == 'Z':
            return 6
    if opponent == 'C':
        if self == 'X':
            return 6
        if self == 'Y':
            return 0
        if self == 'Z':
            return 3


total = 0
self_value = 0
for line in file.readlines():
    line = line.split(" ")
    line[1] = line[1].strip()
    result = rps_compare(line[0], line[1])
    self_value = user_guess(line[1])
    total += self_value + result

print(total)
