biggest = 0
current = 0
file = open('input.txt')
for line in file.readlines():
    line = line.strip()
    if line: #checks if input is a value
        line = int(line)
        current += line
    else: #checks for blank space to signify new elf and reset
        if current > biggest:
            biggest = current
        current = 0
file.close()

print(biggest)
