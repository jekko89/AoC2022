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
sceneScore = 0
for x in range(0, x_max):
    for y in range(0, y_max):
        #create variables for trees seen in each direction
        northVis = 0
        southVis = 0
        westVis = 0
        eastVis = 0
        current = treeMap[x][y]
        #check visible north - iterates from current to edge of map
        #note: if edge of map, it doesn't run through these for loops
        for north in range(y-1,-1,-1):
            northVis += 1
            if current > treeMap[x][north]:
                pass
            else:
                break
        #check visible south
        for south in range(y+1,y_max):
            southVis += 1
            if current > treeMap[x][south]:
                pass
            else:
                break
        #check visible west
        for west in range(x-1,-1,-1):
            westVis += 1
            if current > treeMap[west][y]:
                pass
            else:
                break
        #check visible east
        for east in range(x+1,x_max):
            eastVis += 1
            if current > treeMap[east][y]:
                pass
            else:
                break

        #calculate score and compare with highest
        curScore = northVis * southVis * westVis * eastVis
        if curScore > sceneScore:
            sceneScore = curScore


#print total visible trees
print(sceneScore)
