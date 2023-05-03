input_file = open('input.txt', 'r')
#take input
inputMap = input_file.readlines()
x_max = int(len(inputMap[0]))-1
y_max = 0
treeMap = [[]]

#initialize 2d array based on # of columns
for x in range(0, x_max-1):
    treeMap.append([])

#append each line to 2d array
for line in inputMap:
    line = line.strip()
    x = 0
    for tree in line:
        treeMap[x].append(tree)
        x += 1
    y_max += 1

#determine if each tree is visible
visible = 0
for x in range(0, x_max):
    for y in range(0, y_max):
        #create flags for each direction, default to True for the case that they are on the edge of the map
        northVis = True
        southVis = True
        westVis = True
        eastVis = True
        current = treeMap[x][y]
        #check visible north - iterates from current to edge of map
        #note: if edge of map, it doesn't run through these for loops
        for north in range(y-1,-1,-1):
            if current > treeMap[x][north]:
                northVis = True
            else:
                northVis = False
                break
        #check visible south
        for south in range(y+1,y_max):
            if current > treeMap[x][south]:
                southVis = True
            else:
                southVis = False
                break
        #check visible west
        for west in range(x-1,-1,-1):
            if current > treeMap[west][y]:
                westVis = True
            else:
                westVis = False
                break
        #check visible east
        for east in range(x+1,x_max):
            if current > treeMap[east][y]:
                eastVis = True
            else:
                eastVis = False
                break

        #increment if visible
        if northVis == True or southVis == True or westVis == True or eastVis == True:
            visible += 1

#print total visible trees
print(visible)
