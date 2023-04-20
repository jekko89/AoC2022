current = 0
top = [0, 0, 0]
file = open('input.txt')
for line in file.readlines():
    #line = line.strip()
    if line != '\n': #checks if input is a value
        line = int(line)
        current += line
    else: #checks for blank space to signify new elf and reset
        for x in range(len(top)):
            if current > top[x]:
                top.append(current)
                top.sort(reverse=True)
                top.pop()
                break
        current = 0
file.close()

#final check just in case there is no end line
for x in range(len(top)):
            if current > top[x]:
                top.append(current)
                top.sort(reverse=True)
                top.pop()

print(top)
top_total = 0
for i in top:
    top_total += i
print(top_total)
