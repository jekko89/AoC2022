file = open('input.txt', 'r')


def getPriority(character):
    if character == 'a':
        return 1
    if character == 'b':
        return 2
    if character == 'c':
        return 3
    if character == 'd':
        return 4
    if character == 'e':
        return 5
    if character == 'f':
        return 6
    if character == 'g':
        return 7
    if character == 'h':
        return 8
    if character == 'i':
        return 9
    if character == 'j':
        return 10
    if character == 'k':
        return 11
    if character == 'l':
        return 12
    if character == 'm':
        return 13
    if character == 'n':
        return 14
    if character == 'o':
        return 15
    if character == 'p':
        return 16
    if character == 'q':
        return 17
    if character == 'r':
        return 18
    if character == 's':
        return 19
    if character == 't':
        return 20
    if character == 'u':
        return 21
    if character == 'v':
        return 22
    if character == 'w':
        return 23
    if character == 'x':
        return 24
    if character == 'y':
        return 25
    if character == 'z':
        return 26
    if character == 'A':
        return 27
    if character == 'B':
        return 28
    if character == 'C':
        return 29
    if character == 'D':
        return 30
    if character == 'E':
        return 31
    if character == 'F':
        return 32
    if character == 'G':
        return 33
    if character == 'H':
        return 34
    if character == 'I':
        return 35
    if character == 'J':
        return 36
    if character == 'K':
        return 37
    if character == 'L':
        return 38
    if character == 'M':
        return 39
    if character == 'N':
        return 40
    if character == 'O':
        return 41
    if character == 'P':
        return 42
    if character == 'Q':
        return 43
    if character == 'R':
        return 44
    if character == 'S':
        return 45
    if character == 'T':
        return 46
    if character == 'U':
        return 47
    if character == 'V':
        return 48
    if character == 'W':
        return 49
    if character == 'X':
        return 50
    if character == 'Y':
        return 51
    if character == 'Z':
        return 52

total = 0
group = []
counter = 0
for line in file.readlines():
    line = line.strip()
    group.append(line)
    counter += 1
    if counter == 3:
        for a in group[0]:
            for b in group[1]:
                for c in group[2]:
                    if a == b == c:
                        total += getPriority(a)
                        break
                if a == b == c:
                    break
            if a == b == c:
                counter = 0
                group.clear()
                break
print(total)
                
