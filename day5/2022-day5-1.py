#open input file
file = open('input.txt', 'r')

#global variables for program
mapDone = False
stacksMap = []
stacksData = [[]]
directions = []

#stacking problem
#how to properly get inputs and store them?

#inputs
for line in file.readlines():
    #until empty line, that's the map?
    if line.strip():
        if mapDone == False:
            stacksMap.append(line.rstrip('\n'))
        elif mapDone == True:
            directions.append(line.rstrip('\n'))
    else:
        #map is done, now get inputs for directions
        mapDone = True

#set stacks
stacksMap.reverse()
stacksMax = len(stacksMap[0][1::4])

#initialize empty stacks
for y in range(0, stacksMax-1):
    stacksData.append([])

#populate stacks from bottom up
for rows in stacksMap:
    #only taking the input, ignoring the rest of the characters
    rows = rows[1::4]
    index = 0
    for columns in rows:
        if columns.strip():
            stacksData[index].append(columns)
        #increment to next stack
        index += 1
        
#how to read instructions for each movement of stack?
for line in directions:
    line = line.split()
    amount = int(line[1])
    stackFrom = int(line[3])-1
    stackTo = int(line[5])-1
    for x in range(0, amount):
        temp = stacksData[stackFrom][-1]
        stacksData[stackFrom].pop()
        stacksData[stackTo].append(temp)

#output the crate on the top of each stack
answer = ""
for x in range(0, stacksMax):
    answer += stacksData[x][-1]
print(answer)
